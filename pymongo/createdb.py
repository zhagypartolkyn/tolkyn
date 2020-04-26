import pymongo
myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase = myclient["university"]
dblist= myclient.list_database_names()
print(dblist )
#database created

#check for specific databse
if "university" in dblist:
  print("The database exists.")

