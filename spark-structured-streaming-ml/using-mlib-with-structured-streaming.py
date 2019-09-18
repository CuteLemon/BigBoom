from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

df = spark.read.csv("./aapl-trading-hour.csv", header=True, inferSchema=True)

# data transform
stages = []
numericCols = ["open", "high", "low"]
feature_assembler = VectorAssembler(inputCols=numericCols, outputCol="features")
stages += [feature_assembler]
# label_assembler = VectorAssembler(inputCols=["close"], outputCol="label")
# stages += [label_assembler]

pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
selectedCols = ['close', 'features']
df = df.select(selectedCols)
df.printSchema()

# split to train & test
train, test = df.randomSplit([0.7, 0.3], seed = 2018)
print("Training Dataset Count: " + str(train.count()))
print("Test Dataset Count: " + str(test.count()))

# fit
lr = LinearRegression(maxIter=5, regParam=0.0, solver="normal",labelCol='close')
lrModel = lr.fit(train)

trainingSummary = lrModel.summary
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)

train.describe().show()

# get prediction
lr_predictions = lrModel.transform(test)
lr_predictions.select("prediction","close","features").show(5)


# R2 on test
lr_evaluator = RegressionEvaluator(predictionCol="prediction", \
                 labelCol="close",metricName="r2")
print("R Squared (R2) on test data = %g" % lr_evaluator.evaluate(lr_predictions))

"""
TODO:
get a dymamic data with streaming data.

eg.
R2 on test.
prediction & close price in the same chart.
"""
