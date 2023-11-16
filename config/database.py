from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.foms_db
    collection = db["form_templates"]

except Exception as e:
    print("Connection to database error")
    print(e)
