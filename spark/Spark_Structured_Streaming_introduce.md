# Spark Structured Streaming 介绍

## Overview

Spark Stuctured Streaming 是一个建立在Spark SQL 引擎之上的**高扩展、高容错**的流处理引擎。它提供和批处理一致的语法接口，使用户不需要对流数据和批数据分别处理。

Spark Structured Streaming VS Spark Streaming 

Structured Streaming 有两种工作模式：

1. Micro-batch Processing微批处理，最低100ms 延迟，提供恰好一次的语义保证
2. Continuous Processing连续处理[^1]，最低1ms 延迟，提供最少一次的语义保证

#### 微批处理

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()
    
# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words.groupBy("word").count()
# Start running the query that prints the running counts to the console
query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
```

几种输出模式

1. Completed Mode 每次处理将全量结果输出。
2. Append Mode 每次处理将新增的结果行输出，这要求之前的得到的结果不能改变。数据只有新增，不会有（历史数据的）更新。
3. Update Mode 每次处理将更新过的数据行输出。

Stuctured Streaming 并不保留全量数据表。以聚合运算sum为例，每次有新数据到来时，Structured Streaming 引擎并不会重新从第一行计算到最后一行。它会机智的使用上一次的运算结果去简化运算过程。

求和

**process 1**: $data_1 = 1$ , $sum_1=\sum(data_1) = 1$ 

**process 2**: $data_2 = 2$ , $sum_2=sum_1+\sum(data_2)$

**process 3**: $data_3 = 3$ , $sum_3 = sum_2 + \sum(data_3)$

...

求均值

**process 1**:	 $data_1 = 1$

- $sum_1 = 1$	

- $cnt_1=1$

- $avg_1 = sum_1/cnt_1 = 1$

  

**process 2**: 	$data_2 = [2,3,4]$

- $sum_2 = sum_1+\sum(data_2)$

- $cnt_2 = cnt1 + count(data_2)$
- $avg_2 = sum_2/cnt_2 = 2.5$

...

Structured Streaming 针对无边界的表模型，它总是使用迭代算法而非全量计算。在此过程中，用户不需要去管理中间状态，引擎已经帮你处理好，使得你不用去关心中间变量的更新、至少一次/恰好一次的语义实现、错误恢复等一些列头疼的问题。

**一些不支持的运算**

1. 链式聚合运算
2. limit / top N rows
3. Distinct
4. Sorting (除了complte mode )
5. 其他



#### 连续处理

只需要增加一行代码即可解锁：

1. 低至1ms 的处理延时
2. 至少一次的语义保证

```python
spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load() \
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("topic", "topic1") \
  .trigger(continuous="1 second") \     # only change in query
  .start()
```

微批处理与连续处理的转化仅仅只需要增删一行代码即可。这么好的功能，有什么不完美的地方呢？截止2019-09-30，Spark 2.4.4 下，**不支持以下功能**：

1. 聚合函数
2. current_date() / current_time() (因为计算延迟无法保证)
3. 输入除了kafka 以外的数据源（测试可以使用 rate source 生成数据)
4. 输出除了kafka 以外的存储方式 (测试可以输出到内存/控制台)
5. 失败重试（一此任务处理挂了都会导致直接退出，需要手动从检查点重新启动）



## Storm、Spark、Flink的对比

|                    | Storm             | Spark Streaming[^3] | Spark Structured Streaming[^2] | Flink                           |
| ------------------ | ----------------- | ------------------- | ------------------------------ | ------------------------------- |
| 核心处理模式       | 流处理            | 微批处理            | 流处理                         | Streaming/batch                 |
| 延迟量级           | ms                | s                   | ms                             | ms                              |
| 是否自带机器学习库 | 否                | 是                  | 是                             | 是                              |
| 滑动时间窗口支持   | 不支持            | 否                  | 支持                           | 支持                            |
| 单节点TPS          | 低                | 高                  | 高                             | 高                              |
| 语义               | 恰好一次/至少一次 | 恰好一次            | 至少一次                       | 恰好一次                        |
| 容错               | 中                | 高                  | 中                             | 中                              |
| 部署               | JRE + Zookeepr    | JRE                 | JRE                            | JRE                             |
| 社区               | 5K Stars          | 23K                 | 新事物                         | 10K Stars                       |
| 适合场景           | 供起来            | 流式ETL             | 在等等                         | 低延迟流处理系统(完全取代Strom) |



## 参考链接

[Spark 官方文档](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)

[Apache 流框架 Flink，Spark Streaming，Storm对比分析](https://bigdata.163yun.com/product/article/5)



[^1]:Spark 2.3+以后提供
[^2]: Continuous Processing 模式
[^3]: 使用Spark Structured Streaming 下的 Micro-bath Processing 模式

