from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
         dag_id='primera_orquestation',
         schedule_interval='@daily',
         start_date=datetime(2024,1,1),
         end_date=datetime(2024,1,10),
         default_args={'depends_on_past':True},
         max_active_runs=1
         ) as dag:
    
    t1 = BashOperator(task_id='task1',
                      bash_command='sleep 2 && echo "Holiwis"')
    t2 = BashOperator(task_id='task2',
                      bash_command='sleep 2 && echo "Holiwis"')
    t3 = BashOperator(task_id='task3',
                      bash_command='sleep 2 && echo "Holiwis"')
    t4 = BashOperator(task_id='task4',
                      bash_command='sleep 2 && echo "Holiwis"')
    t5 = BashOperator(task_id='task5',
                      bash_command='sleep 2 && echo "Holiwis"')
    
    t1 >> [t2,t3] >> t4 >> t5