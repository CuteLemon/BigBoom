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

ds = df\
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode("Append") \
    .format("console").option("checkpointLocation","./checkpoint/") \  
    .start()

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

ds = df\
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .outputMode("Append") \
  .format("console").start()

ds = df\
  .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .outputMode("Append") \
  .format("csv").option("path", "path/to/destination/dir").option("checkpointLocation","./checkpoint/").start()

schema = StructType([StructField("t", BinaryType(), True),  # name， type, nullable
                      StructField("c2", IntegerType(), True)])

schema = StructType().add('a',StringType()).add('b',IntegerType()) 
from_json("{'a':'songxx','b':4}",schema)

# 返回空值是因为无法解析
pyspark.sql.functions.from_json(col, schema, options={})
Parses a column containing a JSON string into a [[StructType]] with the specified schema.
  Returns null, in the case of an unparseable string.