## 数据缓冲


### Kafka + Spark Streaming
v0.01

spark 2.3以后 对 kafka 0.8 已经放弃支持。
使用spark 2.4.4 作为开发版本。
```bash
# 启动Spark 集群
cd spark/docker-spark
docker-compose up
# 启动kafka 集群
cd kafka/kafka-docker
docker-compose -f docker-compose-single-broker.yml up
```

```python
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
        print(o.topic, o.partition, o.fromOffset,o.untilOffset)
        # TODO: 可以修改为更时尚的计数值、均值等数值指标

 directKafkaStream.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)

 ssc.start()
 ssc.awaitTermination()
```
在金融支付领域使用 RabbitMQ 居多，而在日志处理、大数据等方面 Kafka 使用居多。

### RabbitMQ

FAQ
pyspark 2.4.2版本问题导致无法使用pyspark 调用对应的kafka jar包。(安装相应的包也不行)
使用pyspark 2.4.4并安装相应的jar 包后解决问题。[下载链接](https://search.maven.org/classic/#search%7Cgav%7C1%7Cg%3A%22org.apache.spark%22%20AND%20a%3A%22spark-streaming-kafka-0-8-assembly_2.11%22)

参考资料
1. [消息中间件 Kafka 与 RabbitMq 的对比](https://www.infoq.cn/article/kafka-vs-rabbitmq)
2. [Databricks Data Streaming](https://stanford.edu/~rezab/sparkclass/slides/td_streaming.pdf)