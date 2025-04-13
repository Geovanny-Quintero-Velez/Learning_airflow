from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
from datetime import datetime

default_args={'depends_on_past':True}

def myfunction(**context):
    print( int(context['ti'].xcom_pull(task_ids='task2')) - 24 )

with DAG(dag_id='xcom_dag',
         description='dag using cross communication',
         start_date=datetime(2025,4,12),
         max_active_runs=1,
         schedule_interval='@once',
         default_args=default_args
         ) as dag:
    
    t1 = BashOperator(task_id='task1',
                      bash_command='sleep 5 && echo $((3 * 8))'
                      )
    
    t2 = BashOperator(task_id='task2',
                      bash_command='sleep 3 && echo {{ ti.xcom_pull(task_ids="task1") }}'
                      )
    
    t3 = PythonOperator(task_id='task3',
                        python_callable=myfunction
                        )
    
    t1 >> t2 >> t3