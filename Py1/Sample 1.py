from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import StructType, StructField, StringType

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sqlContext = SQLContext(SparkContext)
df = sqlContext.read.json("https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json")

df.show()

