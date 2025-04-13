from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(
    dag_id='file_sensor_dag',
    description='file sensor dag',
    start_date=datetime(2025,4,12),
    schedule_interval='@once',
    max_active_runs=1
) as dag:
    
    t1 = BashOperator(task_id='file_creator_task',
                      bash_command='sleep 10 && touch /tmp/textfile.txt')
    
    s1 = FileSensor(task_id='file_checker_task',
                    filepath='/tmp/textfile.txt',
                    poke_interval=20)
    
    t2 = BashOperator(task_id='last_operation_task',
                      bash_command='echo "operation succeed"')
    
    [t1,s1] >> t2