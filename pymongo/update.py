import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

myquery = { "faculty": "ISE" }
newvalues = { "$set": { "faculty": "IT" } }

mycollection .update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycollection .find():
  print(x)