## 数据缓冲

kafka / Rabbitmq

v0.01
- 使用kafka 作为数据缓冲层
- kafka + spark-streaming 

spark 2.3以后 对 kafka 0.8 已经放弃支持。
使用spark 2.4.4 作为开发版本。
```bash
# 启动Spark 集群
spark-docker 的 worker / master 是两个版本？
# 启动kafka 集群
```

```python
spark-streaming-kafka-0-10-assembly_2.12-2.4.2.jar
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext

ssc = StreamingContext(sc, 3)

directKafkaStream = KafkaUtils.createDirectStream(ssc,['test'],{"bootstrap.servers":'localhost:9092'})

offsetRanges = []

 def storeOffsetRanges(rdd):
     global offsetRanges
     offsetRanges = rdd.offsetRanges()
     return rdd

 def printOffsetRanges(rdd):
     for o in offsetRanges:
         print("%s %s %s %s")% (o.topic, o.partition, o.fromOffset, o.untilOffset)

 directKafkaStream \
     .transform(storeOffsetRanges) \
     .foreachRDD(printOffsetRanges)
```
在金融支付领域使用 RabbitMQ 居多，而在日志处理、大数据等方面 Kafka 使用居多。

FAQ
spark 2.4.2版本问题导致无法使用pyspark 调用对应的kafka jar包。(安装相应的包也不行)
使用pyspark 2.4.4并安装相应的jar 包后解决问题。

参考资料
1. [消息中间件 Kafka 与 RabbitMq 的对比](https://www.infoq.cn/article/kafka-vs-rabbitmq)