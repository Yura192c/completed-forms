from pymongo import MongoClient
import os

host = os.environ.get('MONGODB_HOST', 'localhost')
port = os.environ.get('MONGODB_PORT','27017')
client = MongoClient(f"mongodb://{host}:{port}")

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.foms_db
    collection = db["form_templates"]

except Exception as e:
    print("Connection to database error")
    print(e)
