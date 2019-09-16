from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import from_json
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("StructuredStreaming_Kafka") \
    .getOrCreate()

# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "test") \
  .option("fetchOffset.retryIntervalMs","3000") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

ds = df \
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("topic", "test") \
  .option("checkpointLocation","./checkpoint/") \
  .start()

# output to console with string parse
ds = df\
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode("Append") \
    .format("console").option("checkpointLocation","./checkpoint/") \  
    .start()

# output to console with json parse
schema = StructType().add("timestamp", DateType())\
  .add("open", IntegerType()) \
  .add("high", IntegerType()) \
  .add("low", IntegerType()) \
  .add("close", IntegerType()) \
  .add("volume", IntegerType()) 

df.select( \
  df["key"].cast("string"),
  from_json(df["value"].cast("string"), schema)) \
  .writeStream \
  .outputMode("Append") \
  .format("console").start()

# output to csv
ds = df\
  .selectExpr(df["key"].cast("string"),
                from_json(df["value"].cast("string"), schema)) \
  .writeStream \
  .outputMode("Append") \
  .format("csv") \
  .option("path", "./csv_output/") \
  .option("checkpointLocation","./checkpoint/") \
  .start()