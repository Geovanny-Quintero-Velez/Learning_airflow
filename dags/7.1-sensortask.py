from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(
    dag_id='second_step_sensor_dag',
    description='Primary sensor dag',
    start_date=datetime(2025,4,12),
    schedule_interval='@once',
    max_active_runs=1
) as dag:
    
    s1 = ExternalTaskSensor(task_id='waiting_task',
                            external_dag_id='first_step_sensor_dag',
                            external_task_id='task_pointed_by_sensor',
                            poke_interval=5 #Seconds to wait until ask for task accomplishment
                            )
    
    t1= BashOperator(task_id='action_after_waiting_task',
                     bash_command='echo "Task after waiting triggered"'
                     )
    
    s1 >> t1