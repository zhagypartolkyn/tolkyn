import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase= myclient["university"]
mycollection = mydatabase["faculty"]


mycollection.drop()

#The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.