from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG("base_dag_fzs", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="touch_shared_folder_file", bash_command="touch $HOME/data/korte.py", dag=dag)

t2 = BashOperator(task_id="execute_docker_container_on_host", bash_command="docker run dummy-script:v1 python app/main.py", retries=3, dag=dag)
t2.set_upstream(t1)