from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

# pass this to "raise exception" to induce an error
def myfunction():
    pass

default_args={}

with DAG(dag_id="6.2-monitoring",
        description="Monitoreando nuestro DAG",
        schedule_interval="@monthly",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 5, 1),
        default_args=default_args,
        max_active_runs=1
        ) as dag:


    t1 = BashOperator(task_id="tarea1",
                    bash_command="sleep 2 && echo 'Primera tarea!'",
                    depends_on_past=False,
                    retries=2,
                    retry_delay=5,
                    trigger_rule=TriggerRule.ALWAYS
                    )

    t2 = BashOperator(task_id="tarea2",
                    bash_command="sleep 2 && echo 'Segunda tarea!'",
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True,
                    trigger_rule=TriggerRule.ONE_SUCCESS
                    )

    t3 = BashOperator(task_id="tarea3",
                    bash_command="sleep 2 && echo 'Tercera tarea!'",
                    retries=2,
                    retry_delay=5,
                    depends_on_past=False,
                    trigger_rule=TriggerRule.ALWAYS
                    )

    t4 = PythonOperator(task_id="tarea4",
                    python_callable=myfunction,
                    retries=2,
                    retry_delay=5,
                    depends_on_past=False,
                    trigger_rule=TriggerRule.ALL_SUCCESS)

    t5 = BashOperator(task_id="tarea5",
                    bash_command="sleep 2 && echo 'Quinta tarea!'",
                    retries=2,
                    retry_delay=5,
                    depends_on_past=True,
                    trigger_rule=TriggerRule.ALL_FAILED)


    t1 >> t2 >> t3 >> t4 >> t5