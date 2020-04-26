import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

mydoc = mycollection.find().sort("name")
#Sort the result alphabetically by name:
for x in mydoc:
  print(x)