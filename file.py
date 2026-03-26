import pymongo
conn=pymongo.MongoClient("mongodb://localhost:27017/")
#print(conn.list_database_names())
db=conn["student"]
#print(db.list_collection_names())
col=db["mark"]
data={"rollno":12,"name":"devika","marks":45}
x=col.insert_one(data)
if(x):
    print(" data inserted")
else:
    print("failed")

