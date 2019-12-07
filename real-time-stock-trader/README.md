## 实时股票交易系统

实时数据接收器 -> 交易所数据缓存 -> 数据处理引擎 -> 数据缓存 -> 离线数据存储 / 交易策略实时计算 -> 交易执行模块 -> 实时监控看板

实时数据接收器
    - 使用离线历史数据产生 python pandas
    - 调取实时数据接口

交易所数据缓存
kafaka/rabbitmq

数据处理引擎
spark streaming + SparkML
flink
python sklearn
tensorflow

指令数据缓存
redis

离线存储
csv - 交易预测数据，交易指令数据
postgresql
mongodb

交易执行模块
富途牛牛模拟仓API

实时监控模块
ELK 数据看板 - 持仓数据，指令数据，指令结果，价格预测

开发历史
9.10
完成spark streaming + kafaka intergration demo v0.01 . 

TODO： 
使用历史股票数据模拟发送。
Spark streaming 计算股票价格的5分钟滑动均值作为预测值。

stock_price$\stackrel{Kafka}\Longrightarrow$ store $\stackrel{pythonlog}\Longrightarrow$ ELK
stock_price$\stackrel{Kafka}\Longrightarrow$ predict $\stackrel{pythonlog}\Longrightarrow$ ELK

数据存储使用Python 脚本, 存储数据的同时logging 将数据发送到 logstash
数据预测使用pyspark 脚本,计算数据的同时logging 将数据发送到 logstash

数据预测使用 Spark ML
9.11
完成历史股票数据模拟发送。

直接从kafka + Spark Streaming 架构中读取kafaka 的message 没有找到快速验证的方案。
使用 Spark Structured Streaming(DataFrame) 去替换 Spark Streaming (DStreams)

9.16
使用 Spark Structured Streaming 成功从kafka 中解析DataFrame.         

Spark Streaming Machine Learning
https://towardsdatascience.com/realtime-prediction-using-spark-structured-streaming-xgboost-and-scala-d4869a9a4c66

12.5 TODO: 将计算值output 放入Kafka 队列。