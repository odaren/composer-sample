import datetime

import airflow
from airflow import models
from airflow.contrib.operators import bigquery_operator
from airflow.contrib.operators import gcs_to_bq

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    'owner': 'airflow',
    'start_date': YESTERDAY,
}

with models.DAG(
    dag_id='gcs_to_bq_sample',
    default_args=default_args,
    schedule_interval=None # スケジュール例'0 * * * *'
    ) as dag:

    # データセットを作成するタスク
    create_dataset = bigquery_operator.BigQueryCreateEmptyDatasetOperator(
        task_id='create_dataset',
        dataset_id='composer_test_dataset',
        dag=dag
    )

    # GCSから、BQテーブルに、データをロードするタスク
    load_csv = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
        task_id='load_csv',
        bucket='',
        source_objects=['sample_data.csv'],
        destination_project_dataset_table='tcomposer_test_dataset.composer_test_table',
        write_disposition='WRITE_TRUNCATE',
        autodetect=True,
        dag=dag
    )

 # 依存関係
create_dataset >> load_csv
