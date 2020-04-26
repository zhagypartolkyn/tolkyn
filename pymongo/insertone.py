import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase= myclient["university"]
mycollection = mydatabase["fit"]

mydict = { "name": "Tolkyn", "surname": "Zhagypar", "faculty":"IT" }

x = mycollection.insert_one(mydict)
