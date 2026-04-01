'''import pymongo 
conn=pymongo.MongoClient("mongodb://localhost:27017/") 
#print(conn.list_database_names()) 
# db=conn["student"]
# #print(db.list_collection_names())
# col=db["mark"] 
# data={"rollno":12,"name":"devika","marks":45}
# x=col.insert_one(data)
# if(x): 
# print(" data inserted")
# else: 
# print("failed")'''



# List of multiple documents
'''data = [
 #   {"rollno": 12, "name": "devika", "marks": 45},
    {"rollno": 13, "name": "arun", "marks": 67},
    {"rollno": 14, "name": "meera", "marks": 89},
    {"rollno": 15, "name": "rahul", "marks": 76},
    {"rollno": 16, "name": "sneha", "marks": 55}
]

# Insert multiple records
x = col.insert_many(data)

if x.inserted_ids:
    print("Data inserted successfully")
else:
    print("Failed to insert")'''
    
    
#for i in col.find():
 #   print(i)
'''for i in col.find({}, {"name": 1, "_id": 0}).sort({"marks": -1}):
    print(i)
top_student = col.find().sort("marks", -1).limit(1)

for i in top_student:
    print(i["name"])'''
'''data = [
 #   {"rollno": 12, "name": "devika", "marks": 45},
    {"rollno": 13, "name": "arun", "mark1": 67,"mark2":56,"mark3":78},
    {"rollno": 14, "name": "meera", "mark1": 89,"mark2":46,"mark3":76},
    {"rollno": 15, "name": "rahul", "mark1": 76,"mark2":86,"mark3":97}
]
x = col.insert_many(data)

if x.inserted_ids:
    print("Data inserted successfully")
else:
    print("Failed to insert")
    
'''

import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["college1"]
col = db["studlist1"]

for i in col.find({}, {"_id": 0}):
    total = i["mark1"] + i["mark2"] + i["mark3"]
    print("Name:", i["name"], "Total Marks:", total)

for i in col.find(
        {"name": {"$regex": "^a"}},  
        {"name": 1, "_id": 0}        
    ).sort([("name", -1)]):           
    print(i["name"])

col.delete_one({"rollno":13})'''

'''result = col.find(
    {"gender": "female", "course": "MCA"},
    {"name.fname": 1, "name.lname": 1, "mark": 1, "_id": 0}
)
                                                                                #1
for doc in result:
    print(doc)
    
result = col.find({"course": "MCA"}).sort("mark", -1).limit(1)

for doc in result:
    print(doc)                                                                      #2


result = col.find({"gender": "male", "grade": "A+"})

for doc in result:
    print(doc)                                                                            #3
    
result = col.find(
    {"course": "Mechanical"},
    {"name.fname": 1, "name.lname": 1, "_id": 0}
).sort("mark", -1).limit(3)

for doc in result:
    print(doc)                                                                       #4
    
result = col.find(
    {"gender": "female", "mark": {"$gt": 90}},
    {
        "name.fname": 1,
        "name.lname": 1,
        "grade": 1,
        "mark": 1,
        "phone": 1,
        "_id": 0
    }
)

for doc in result:
    print(doc)                                                                #5
 
result = col.find({"mark": {"$gt": 80, "$lt": 90}})

for doc in result:
    print(doc)                                                              #6

result = col.find({"name.fname": {"$regex": "^V", "$options": "i"}})

for doc in result:
    print(doc)                                                           #7
    
    
result = col.find({"address.city": "Kollam"})

for doc in result:
    print(doc)                                                   #8
    
result = col.find({
    "address.city": {"$nin": ["Kollam", "Thiruvananthapuram"]}
})

for doc in result:
    print(doc)                                                    #9
    
result = col.find({
    "gender": "female",
    "address.city": {"$in": ["Kollam", "Thiruvananthapuram"]}
})

for doc in result:
    print(doc)                                                                    #10