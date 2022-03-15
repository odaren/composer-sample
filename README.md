# composer-sample
Cloud Composesrで、GCSにあるデータを、BigQueryテーブルにロードするサンプル

## Cloud Composesrとは
ワークフロー管理ツールであるAirflowのマネージドサービス。   
データ分析基盤におけるワークフローとは、データの取り込み・加工・集計といった一連の処理のこと。  
Composer(Airflow)では、ワークフローの各タスクをPythonで定義する。  

## やること
以下の２つのジョブを実行するワークフローを定義し、Composerで実行する。
1. BigQueryデータセットを作成する。
2. GCSにあるデータを、BigQueryテーブルにロードする。

## 手順
