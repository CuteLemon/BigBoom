## Aiflow
Airflow 是一款虽然不是设计用来做ETL，但被广泛用来做ETL的工具。
ETL说人话即做数据的清洗、同步、与转移。


```bash
docker pull puckel/docker-aiflow:1.10.4

docker run -d -p 8080:8080 puckel/docker-airflow webserver
```

TODO:
* [x]  airflow container 与host 共享 ./dags/* 下的文件。
* [ ] 一个Python Operator 的example.
* [ ] 一个postgreSQL Operator 的example.
* [ ] 使用插件的🌰
* [ ] 多个task 的级联example.

#airflow plugin
如何制作插件
1. 首先查看社区是否有成熟的插件，避免重复造轮子
2. 

task 的边界
1. 一次只做一件事情
2. 可以高度并行化