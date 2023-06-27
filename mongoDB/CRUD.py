from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection details
client = MongoClient()

# Access the database and collection
db = client.get_database("your_database_name")
collection = db.get_collection("your_collection_name")

@app.route("/create", methods=["POST"])
def create_document():
    data = request.get_json()
    # Insert the document into the collection
    result = collection.insert_one(data)
    return jsonify({"message": "Document created", "id": str(result.inserted_id)}), 201

@app.route("/read", methods=["GET"])
def read_documents():
    documents = collection.find()
    # Convert the cursor to a list of documents
    document_list = list(documents)
    return jsonify(document_list), 200

@app.route("/update/<id>", methods=["PUT"])
def update_document(id):
    data = request.get_json()
    # Update the document that matches the given id
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count == 0:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Document updated"}), 200

@app.route("/delete/<id>", methods=["DELETE"])
def delete_document(id):
    # Delete the document that matches the given id
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Document deleted"}), 200

if __name__ == "__main__":
    app.run()
