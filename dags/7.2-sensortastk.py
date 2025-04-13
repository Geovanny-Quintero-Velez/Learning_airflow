from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id='first_step_sensor_dag',
         description='dag_pointed_by_sensor',
         start_date=datetime(2025,4,12),
         schedule_interval='@once',
         max_active_runs=1
         ) as dag:
    
    t1 = BashOperator(task_id='task_pointed_by_sensor',
                      bash_command='sleep 10 && echo "Condition for sensor accomplished"'
                      )