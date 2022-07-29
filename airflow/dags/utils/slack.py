from datetime import datetime
from slack_sdk import WebClient

class SlackAlert:
    def __init__(self, channel, token):
        self.channel = channel
        self.client = WebClient(token=token)


    def slack_alarm_success(self, context):
        text = f"""
            date: {datetime.today().strftime('%Y-%m-%d')}
            logs: 
                Success! 
                task id: {context.get('task_instance').task_id}, 
                dag id: {context.get('task_instance').dag_id},
                run_id: {context.get('task_instance').run_id},
                start_date: {context.get('task_instance').start_date},
                duration: {context.get('task_instance').duration},
                log url: {context.get('task_instance').log_url}
            """
        self.client.chat_postMessage(channel=self.channel, text=text)
        

    def fail_msg(self, context):
        text = f"""
            date: {datetime.today().strftime('%Y-%m-%d')}  
            logs: 
                Fail!
                task id: {context.get('task_instance').task_id}, 
                dag id: {context.get('task_instance').dag_id},
                run_id: {context.get('task_instance').run_id},
                start_date: {context.get('task_instance').start_date},
                duration: {context.get('task_instance').duration},
                log url: {context.get('task_instance').log_url}
            """
        self.client.chat_postMessage(channel=self.channel, text=text)