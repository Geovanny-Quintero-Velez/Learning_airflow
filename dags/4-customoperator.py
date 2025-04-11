from airflow import DAG
from operators.custom import HelloOperator
from datetime import datetime

with DAG(dag_id='custom_operator',
         schedule_interval='@once',
         start_date=datetime(2024,6,1)
         ) as dag:
    
    t1 = HelloOperator(task_id='custom_task',
                        name='Geovanny')
    
    t1