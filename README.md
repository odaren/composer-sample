# composer-sample
Cloud Composesrで、GCSにあるデータを、BigQueryテーブルにロードするサンプル

## Cloud Composesrとは
ワークフロー管理ツールであるAirflowのマネージドサービス。   
データ分析基盤におけるワークフローとは、データの取り込み・加工・集計といった一連の処理のこと。  
Composer(Airflow)では、ワークフローの各タスクをPythonで定義する。  

## やること
以下の２つのジョブを実行するワークフローを定義し、Composerで実行する。
1. BigQueryデータセットを作成する。
2. GCSにあるサンプルデータを、BigQueryテーブルにロードする。

## 手順
### Composesrの環境作成
環境を作成する。  
composerのバージョンは、「２」を選択する。  
### GCSバケットの作成
サンプルデータを保存するためのGCSバケットを作成する。  
作成後、「sample_data.csv」をアップロードする。
### DAGのアップロード
環境作成によって自動作成されるDAG用のGCSバケットに、「gcs_to_bq.py」をアップロードする。
### DAGの実行
airflowのwebUIから、DAGを実行する。  
成功すると、BigQueryデータセットにテーブル「composer_test_table」が作成される。
