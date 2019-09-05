from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'max',
    'start_date': datetime(2019, 8, 12),
}

dag = DAG('python_example',
          default_args=default_args,
          description='run python script with Airflow',
          schedule_interval=None
        )

def print_context(ds, **kwargs):
    # pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)