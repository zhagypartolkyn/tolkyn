import pymongo
myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydb = myclient["mydatabase"]
myclient.list_database_names()
dblist = myclient.list_database_names()

mycollection=mydb['calculus']
collection_list=mydb.list_collection_names()

#mydict = { "name": "Tolkyn", "university": "KBTU" }

#x = mycollection.insert_one(mydict)
# print(x.inserted_id)

mylist = [
  { "name": "Temirlan", "address": "Apple st 652"},
  { "name": "Aruzhan", "address": "Mountain 21"},
  { "name": "Nastya", "address": "Valley 345"},
  { "name": "Madina", "address": "Ocean blvd 2"},
  { "name": "Erma", "address": "Green Grass 1"},
  { "name": "Nurdaulet", "address": "Sky st 331"},
  { "name": "Aldik", "address": "One way 98"},
  { "name": "Vika", "address": "Yellow Garden 2"},
  { "name": "Beka", "address": "Park Lane 38"},
  { "name": "Saltanat", "address": "Central st 954"},
  { "name": "Abylay", "address": "Main Road 989"},
  { "name": "Amina", "address": "Sideway 1633"}
] 

y=mycollection.insert_many(mylist)

#find = mycollection.find_one()
#print(find)         


#for list in mycollection.find():
#    print(list)

#myquery = { "address": "Park Lane 38" }
#mydoc = mycollection.find(myquery)
#for doc in mydoc:
#  print(doc)

#z=mycollection.delete_many({})
#print(z.deleted_count, " documents deleted.")

#mycollection.drop()          drops collection

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycollection.update_one(myquery, newvalues)

#print "" after the update:
for query in mycollection.find():
  print(query)