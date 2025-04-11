from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="dag1",
    description="Mi primer dag",
    start_date=datetime(2025,6,1),
    schedule_interval="@once",
) as dag1:
    op = EmptyOperator(task_id="dummy")

dag2 = DAG(
    dag_id="dag2",
    description="Mi segundo dag",
    start_date=datetime(2025,6,1),
    schedule_interval="@once",
)
op2 = EmptyOperator(task_id="dummy2", dag=dag2)

@dag(
    dag_id="dag3",
    description="Mi tercer dag",
    start_date=datetime(2025,6,1),
    schedule_interval="@once",
)
def generate_dag():
    op3 = EmptyOperator(task_id="dummy3")

dag3 = generate_dag()