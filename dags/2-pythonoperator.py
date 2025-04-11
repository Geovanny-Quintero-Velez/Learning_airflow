from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


def print_hello():
    print('Hello people from python funtion')

with DAG(
    dag_id='python_operator',
    description='Fisrt dag using python operator',
    schedule_interval='@once',
    start_date=datetime(2022,8,1)
    ) as dag:
    
    t1 = PythonOperator(
        task_id = 'hello_with_python',
        python_callable = print_hello
    )

def print_country(country, **kwargs):
    print(f'I am processing this {country}')

with DAG(dag_id='pythonoperator'
         , description ='using python operator'
         , start_date=datetime(2023,6,7)
         , schedule_interval='@once') as dag:
    
    t1 = PythonOperator(task_id='process_ar'
                        , python_callable=print_country
                        , op_kwargs= {'country':'AR'})
    
    t2 = PythonOperator(task_id='process_uy'
                        , python_callable=print_country
                        , op_kwargs= {'country':'UY'})
    
    t1 >> t2