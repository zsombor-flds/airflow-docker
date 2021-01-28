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
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("pararell_test", default_args=default_args, schedule_interval=timedelta(1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id="print_date1", bash_command="date", dag=dag)
t2 = BashOperator(task_id="sleep", bash_command="sleep 5", retries=3, dag=dag)
t3 = BashOperator(task_id="print_date2", bash_command="date", dag=dag)
t4 = BashOperator(task_id="print_date3", bash_command="date", dag=dag)

t1 >> [t2, t3] >> t4