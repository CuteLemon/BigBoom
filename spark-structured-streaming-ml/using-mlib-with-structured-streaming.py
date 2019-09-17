from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

df = spark.read.csv('./aapl-trading-hour.csv',
                    header=True, inferSchema=True)
TODO:
df -> train & test

train_csv -> read -> transform -> train -> model 

test_csv -> readstream -> model fit -> predict 
-> realtime output correct rate.