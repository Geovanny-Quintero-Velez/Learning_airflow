from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date

default_args = {'start_date':datetime(2025,3,25) , 'end_date':datetime(2025,4,12)}

def _choose(**context):
    if context['logical_date'].date() < date(2025,4,2):
        return 'finish_1_april'
    return 'start_2_april'

with DAG(dag_id='10-branchPythonOperators',
         schedule_interval='@daily',
         default_args=default_args
         ) as dag:
    
    branching = BranchPythonOperator(task_id='banch-operator',
                                     python_callable=_choose
                                     )
    
    finish_1= BashOperator(task_id='finish_1_april',
                            bash_command='echo "Running {{ds}}"'
                            )

    start_2 = BashOperator(task_id='start_2_april',
                            bash_command='echo "Running {{ds}}"'
                            )
    
    branching >> [finish_1, start_2]
