from pymongo.mongo_client import MongoClient

# Replace the placeholder with your Atlas connection string
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)