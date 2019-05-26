#!/usr/bin/python


from datetime import  datetime
from pyspark.sql import HiveContext, SparkSession
from pyspark import SparkContext, SparkConf

spark = SparkSession.builder.appName("test-task2").enableHiveSupport

sc = spark.SparkContext

rdd = sc.jsonfile("https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json")
