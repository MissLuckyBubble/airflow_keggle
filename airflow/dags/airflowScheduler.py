from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import app


default_args = {
    'owner': 'Silviq',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 21),  
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 dag_id='DAG-USER-DATA-TRANSFER',
        default_args=default_args,
        schedule_interval='@once', 
        catchup=False
    )

transfer_data = PythonOperator(
    task_id = 'data_transfer_workflow',
    python_callable=app.data_transfer_workflow,
    dag=dag,
)

transfer_data