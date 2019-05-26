from datetime import  datetime
from pyspark.sql import HiveContext, SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *

sc = SparkContext
path = r'''C:\Users\mahi.Mahavir\Downloads\recipes.json'''
peopleDF = SparkContext..json(path)
peopleDF.printSchema()
peopleDF.createOrReplaceTempView("people")
teenagerNamesDF = sc.sql("SELECT * FROM people")
teenagerNamesDF.show()