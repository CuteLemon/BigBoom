from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator


default_args = {
    'owner': 'max',
    'start_date': datetime(2019, 8, 12),
}

dag = DAG('PostgresExample',
          default_args=default_args,
          description='run sql script with Airflow',
          schedule_interval=None,
          params={'maintainer_email':['test@test.com']}
        )

run_this = PostgresOperator(
    task_id='create_the_schema',
    sql = 'CREATE SCHEMA IF NOT EXISTS TEST;\
           CREATE TABLE IF NOT EXISTS TEST.test_time AS (SELECT current_time)',
    postgres_conn_id = 'postgres_default',
    database = 'postgres',
    dag=dag,
)