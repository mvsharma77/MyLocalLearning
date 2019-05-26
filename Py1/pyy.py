from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sc = SparkContext(conf = conf)

def parseLines(text):
    line = text.split(',')
    custId = int(line[0])
    amt = float(line[2])
    return (custId, amt)

sc.wholeTextFiles("test.json").values().map(json.loads)
custRDD = sc.textFile("C:\Users\mahi.Mahavir\Downloads/Alcohol_and_Drug_Abuse_Prevention_Services.csv")
cust = custRDD.map(parseLines)
cust = cust.reduceByKey(lambda x,y: x+y)
cust = cust.map(lambda x: (x[1],x[0])).sortByKey()
results = cust.collect()

for result in results:
    print(result)