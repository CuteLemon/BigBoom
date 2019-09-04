## Aiflow
Airflow 是一款虽然不是设计用来做ETL，但被广泛用来做ETL的工具。
ETL说人话即做数据的清洗、同步、与转移。


```bash
docker pull puckel/docker-aiflow:1.10.4

docker run -d -p 8080:8080 puckel/docker-airflow webserver
```

TODO:
airflow container 与host 共享 ./dags/* 下的文件。
一个Python Operator 的example.
一个postgreSQL Operator 的example.
一个AWS - S3 、 Redshift 的example.
多个task 的级联example.
