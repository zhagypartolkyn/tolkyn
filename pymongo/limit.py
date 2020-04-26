import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

myresult = mycollection.find().limit(5)

#print the result:
for x in myresult:
  print(x)