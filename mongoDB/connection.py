from flask import Flask,request
from pymongo import MongoClient


app = Flask(__name__)

# MongoDB Atlas connection details
# Create a MongoClient object and connect to the default host and port
client = MongoClient()

# Alternatively, specify the host and port explicitly
# client = MongoClient("mongodb://localhost:27017")

# Access a database
db = client["JPMC"]

# Access a collection
collection = db["test"]

data = {"name": "John Doe", "age": 25}
collection.insert_one(data)

# Find all documents in the collection
documents = collection.find()

# Iterate over the documents
for document in documents:
    print(document)
# Update a document that matches a specific condition
collection.update_one({"name": "John Doe"}, {"$set": {"age": 30}})
# Delete a document that matches a specific condition
collection.delete_one({"name": "John Doe"})
client.close()


