import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

myquery = { "faculty": "IT" }

mydoc = mycollection.find(myquery)

for x in mydoc:
  print(x)