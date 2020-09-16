from pymongo import MongoClient 
client = MongoClient('localhost', 27017) 
db = client.dbsparta

db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})
print (user)

