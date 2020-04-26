import pymongo

myclient = pymongo.MongoClient('mongodb+srv://pp2:pp2password@cluster0-oevey.mongodb.net/test?retryWrites=true&w=majority')
mydatabase= myclient["university"]
mycollection = mydatabase["faculty"]

mylist = [
  { "name": "Temirlan", "faculty": "IT"},
  { "name": "Aruzhan", "faculty": "VTIPO"},
  { "name": "Nastya", "faculty": "AIU"},
  { "name": "Madina", "faculty": "IT"},
  { "name": "Erma", "faculty": "VTIPO"},
  { "name": "Nurdaulet", "faculty": "NGD"},
  { "name": "Aldik", "faculty": "Business"},
  { "name": "Vika", "faculty": "Foundation"},
  { "name": "Beka", "faculty": "Chemistry"},
  { "name": "Saltanat", "faculty": "IT"},
  { "name": "Abylay", "faculty": "ISE"},
  { "name": "Amina", "faculty": "Business"}
] 


x = mycollection.insert_many(mylist)
print(x.inserted_ids)
