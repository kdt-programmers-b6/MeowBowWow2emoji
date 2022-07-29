from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator


default_args = {
    'owner'                 : 'HyunWoo Oh',
    'description'           : 'ml_workflow',
    'depend_on_past'        : False,
    'start_date'            : datetime(2022, 4, 1),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}


# python main.py --phase 'train' --dataset 'cat_final1' --epoch 100 --iteration 10000 --batch_size 1 --print_freq 1000 --save_freq 10000 --decay_flag True --decay_epoch 50 --lr 0.0001 --GP_ld 10 --adv_weight 1 --cycle_weight 10 --identity_weight 10 --cam_weight 1000 --gan_type 'lsgan' --smoothing True --ch 16 --n_res 4 --n_dis 6 --n_critic 1 --sn True --img_size 256 --img_ch 3 --augment_flag True --checkpoint_dir 'checkpoint_final_cat_v1' --result_dir 'results/cat_final_v1'

# DEF DAG!
with DAG(
    'cat_image_workflow',
    default_args=default_args,
    schedule_interval="@daily",
    concurrency=5,
    catchup=False) as dag:

    # pipeline components !!! 
    start_pipeline = DummyOperator(
    task_id = 'start_pipeline'
    )

    # download cat images to container! 

    # check filed

    # run ml and after alarm! 

    # build docker compose!



