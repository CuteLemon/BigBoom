"""
从Kafka 中读取股价信息，
Spark Streaming 输出10秒时间窗的滑动均值作为预测。
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import from_json
import pyspark.sql.types as spark_type
import pyspark.sql.functions as F
from pyspark.sql.functions import get_json_object
from pyspark.sql.functions import window, avg, count, to_timestamp, col


spark = SparkSession.builder.appName("StructuredStreaming_Kafka").config("spark.sql.shuffle.partitions",2).getOrCreate()

# Subscribe to 1 topic
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "test")
    .option("fetchOffset.retryIntervalMs", "3000")
    .load()
)

# output with window function
ds = (
    df.select(
        get_json_object(df.value.cast("string"), "$.timestamp")
        .cast("timestamp")
        .alias("timestamp"),
        get_json_object(df.value.cast("string"), "$.close")
        .cast("float")
        .alias("close"),
    )
    .groupby(
        window("timestamp", "10 seconds", "1 second")
        .start.cast("string")
        .alias("start_time"),
        window("timestamp", "10 seconds", "1 second")
        .end.cast("string")
        .alias("end_time"),
    )
    .agg(F.avg("close").alias("value"), F.count("close").alias("cnt_close"))
    .where(F.col("cnt_close") == 10)
    .selectExpr("start_time", "end_time", "CAST(value AS STRING)", "cnt_close")
    .writeStream.outputMode("Update")
    # .format("console")
    # .option("truncate", False)
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("topic","output_buffer")
    .option("checkpointLocation", "./checkpoint")
    .start()
)

ds.awaitTermination()
