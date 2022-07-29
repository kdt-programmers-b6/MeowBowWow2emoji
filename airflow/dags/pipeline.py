# python library
from datetime import datetime, timedelta
from utils.slack import SlackAlert
from utils.config import SLACK_BOT_TOKEN, CHANNEL

# airflow operator 
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.task_group import TaskGroup
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.google.cloud.transfers import GoogleDriveToLocalOperator



Slack = SlackAlert(CHANNEL, SLACK_BOT_TOKEN)

default_args = {
    'owner': 'HyunWoo Oh',
    'description': 'ml_workflow',
    'depend_on_past': False,
    'start_date': datetime(2022, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),

}


def _is_container_running(ti):
    tf_container_status = ti.xcom_pull(key='return_value', task_ids=["check_tf-container"])
    if tf_container_status == "running":
        return "running.branch_running"
    else:
        return "branch_not_running"

def _unzip(ti):
    import zipfile
    with zipfile.ZipFile("/opt/airflow/model/images/meow.zip", 'r') as zip_ref:
        zip_ref.extractall("/opt/airflow/model/images/cat_imoji")


# DEFINE DAGs!!!!!
with DAG(
    'cat_image_workflow',
    default_args=default_args,
    schedule_interval="@daily",
    concurrency=5,
    catchup=False,
    on_failure_callback=Slack.slack_alarm_fail) as dag:

    # pipeline components
    start_pipeline = DummyOperator(
    task_id = 'start_pipeline'
    )

    # download cat images to container
    download_from_gdrive_to_local = GoogleDriveToLocalOperator(
        task_id="download_from_gdrive_to_local",
        folder_id="programmers_b6/u-gat-it/emoji/kakao_cat_emoji",
        file_name="cat_emoji.zip",
        output_file="./model/images/meow.zip",
    )

    # check filed
    check_file = FileSensor(
        task_id="check_imoji_file",
        filepath="./model/images/meow.zip"
    )

    # unzip imoji
    unzip_file = PythonOperator(
        task_id="unzip",
        python_callable=_unzip
    )

    # using xcom update container status
    check_container = BashOperator(
        task_id="check_tf_container",
        bash_command="docker inspect -f '{{.State.Status}}' tf-container",
        do_xcom_push=True
    )
    
    # check container is runnig
    branching_status = BranchPythonOperator(
        task_id='branching_container_status',
        python_callable=_is_container_running
    )
    # if not running 
    not_running = BashOperator(
        task_id="branch_not_running",
        bash_command="/opt/airflow/dags/utils/learning.sh",
        on_success_callback=Slack.slack_alarm_success
    )

    # if running
    with TaskGroup(group_id='branch_running') as running:

        running = BashOperator(
            task_id="branch_running",
            bash_command="/opt/airflow/dags/utils/learning_run.sh",
            on_success_callback=Slack.slack_alarm_success
        )
        tf_shutdown = BashOperator(
            task_id="shutdown_tf",
            bash_command="docker container rm tf-container"
        )
        running >> tf_shutdown 

    # just wait all container job finish!
    wait_finish = BashOperator(
        task_id="sleep_30",
        bash_command="sleep 30s"
    )

    # build docker compose!
    build_meowbow = BashOperator(
        task_id="docker_compose",
        bash_command="docker compose up ./meowbow"
    )

    # end pipeline
    end_pipeline = DummyOperator(
    task_id = 'end_pipeline',
    on_success_callback=Slack.slack_alarm_success
    )

    start_pipeline >> download_from_gdrive_to_local >> check_file >> unzip_file >> check_container >> branching_status
    branching_status >> [running, not_running] >> wait_finish >> build_meowbow >> end_pipeline

