from airflow import DAG
from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        dag_id='primer_dag_bash', 
        schedule_interval='@once', 
        start_date=datetime(2025, 7, 1)
    ) as dag:
    t1 = BashOperator(
            task_id='primer_task_bash',
            bash_command='echo "Hola mundo"'
        )