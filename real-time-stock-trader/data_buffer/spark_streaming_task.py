from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkConf,SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("Streaming")
sc = SparkContext(conf = conf)
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

def storeRdd(rdd):
    global kafkaData
    # kafkaData = rdd.KafkaMessageAndMetadata()
    return rdd
def printData(rdd):
    # for d in rdd:
    print(rdd)
# directKafkaStream.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)
directKafkaStream.transform(storeRdd).foreachRDD(printData)

if __name__ == "__main__":
    ssc.start()
    ssc.awaitTermination()