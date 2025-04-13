from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

template_command= """

{% for file in params.filenames %}

    echo '{{ ds }}'
    echo '{{ file }}'

{% endfor %}

"""

with DAG(dag_id='templates',
         description='Example using jinja templates',
         start_date=datetime(2025,4,12),
         schedule_interval='@once',
         max_active_runs=1
         ) as dag:
    
    t1 = BashOperator(task_id='tarea_1',
                      bash_command=template_command,
                      params={'filenames':['filename1.txt','filename2.txt']},
                      depends_on_past=False
                      )