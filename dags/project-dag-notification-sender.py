from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

default_args = {'start_date':datetime(2025,4,13) }


template_command="""

    echo '{{ds}}'

"""

with DAG(dag_id='project_dag_notification_sender',
         schedule_interval='@once',
         default_args=default_args,
         max_active_runs=1
         ) as dag:
    
    t0 = BashOperator(task_id='date_log',
                      bash_command=template_command
                      )
    
    s1 = ExternalTaskSensor(task_id='wait_for_data_integrity_validation',
                            external_dag_id='project_dag_complete_data_files_checker',
                            external_task_id='data_completeness_advisor',
                            poke_interval=30
                            )
    
    t1 = BashOperator(task_id='send_notification',
                      bash_command='echo "Sending notification"'
                      )

    t0 >> s1 >> t1