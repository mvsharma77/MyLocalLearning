
import spark.implicits._


val path = "examples/src/main/resources/people.json"
val peopleDF = spark.read.json("https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json")


peopleDF.printSchema()

peopleDF.createOrReplaceTempView("people")


val teenagerNamesDF = spark.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
teenagerNamesDF.show()

val otherPeopleDataset = spark.createDataset(
    """{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}""" :: Nil)
val otherPeople = spark.read.json(otherPeopleDataset)
otherPeople.show()
