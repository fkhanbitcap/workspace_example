from datetime import timedelta
from datetime import datetime

from airflow import DAG

from airflow.operators.docker_operator import DockerOperator


OWNER = 'Muhammad Faizan Khan'
DESCRIPTION = 'Airflow Workflow Workshop'
DAG_NAME = 'workspace_example' ########## Unique Dag Name for workflow
DOCKER_IMAGE = 'workspace_docker_example' ########## NAME of your docker build
START_DATE = datetime(2021, 4, 12)
CRON_INTERVAL = '0 0/1 * * *'


default_args = {
    'owner': OWNER,
    'description': DESCRIPTION,
    'depend_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'max_active_runs': 1,
    'retry_delay': timedelta(minutes=30)
}


dag = DAG(
    DAG_NAME,
    start_date=START_DATE,
    default_args=default_args,
    schedule_interval=CRON_INTERVAL,
)


t1 = DockerOperator(
    task_id='DockerOperator',
    # command=['-cd', 'none', '-tc', 'SnowflakeLoad'],
    image=DOCKER_IMAGE,
    api_version='auto',
    docker_url="unix://var/run/docker.sock",
    volumes=["/root/.aws:/root/.aws"],
    dag=dag
)
