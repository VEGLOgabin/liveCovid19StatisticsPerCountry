from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Data').getOrCreate()

df=spark.read.csv('covid19.csv',header=True,inferSchema=True)
df.collect()