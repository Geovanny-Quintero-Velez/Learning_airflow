from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
         dag_id='monthly_orquestation',
         schedule_interval='@monthly',
         start_date=datetime(2024,1,1),
         end_date=datetime(2024,2,10)
         ) as dag:
    
    t1 = EmptyOperator(task_id='task1')
    t2 = EmptyOperator(task_id='task2')
    t3 = EmptyOperator(task_id='task3')
    t4 = EmptyOperator(task_id='task4')
    t5 = EmptyOperator(task_id='task5')
    
    t1 >> [t2,t3] >> t4 >> t5