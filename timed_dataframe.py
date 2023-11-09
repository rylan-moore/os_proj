from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import time
from pyspark.sql.functions import col, count, countDistinct

start = time.time()
spark = SparkSession \
    .builder \
    .appName("OS_proj_bench") \
    .master("local[*]")\
    .getOrCreate()

citations = spark.read.load('cite75_99.txt.gz',
            format="csv", sep=",", header=True,
            compression="gzip",
            inferSchema="true")

patents = spark.read.load('apat63_99.txt.gz',
            format="csv", sep=",", header=True,
            compression="gzip",
            inferSchema="true")

cingState = citations.join(patents, citations["CITING"] == patents["PATENT"], how="left")
cingState = cingState.select("CITED", "CITING", col("POSTATE").alias("CitingState"))
# cingState.show(5)

cedState = cingState.join(patents, cingState["CITED"] == patents["PATENT"], how="left")
cedState = cedState.select("CITED", "CITING", "CitingState",col("POSTATE").alias("CitedState"))
cedState = cedState.filter(col("CitingState").isNotNull() & col("CitedState").isNotNull())
cedState = cedState.filter( col("CitingState") == col("CitedState") )
# cedState.show(15)

count_citing = cedState.groupby("CITING").count().orderBy(col("count"), ascending=False)
count_citing = count_citing.select("CITING", col("count").alias("COUNT"))
count_citing.fillna(0)
# count_citing.show(15)

# patents.show(5)
p_output = patents.join(count_citing, count_citing["CITING"]==patents["PATENT"] , how="inner")
# p_output.fillna(0, subset=['COUNT'])
# # p_output.orderBy(col("count"), ascending=False)
p_output = p_output.orderBy(col('COUNT'), ascending=False)
p_output = p_output.drop('CITING')
# p_output.printSchema()
p_output.show(10)
total = time.time() - start
print("Took: %s sec" % total)