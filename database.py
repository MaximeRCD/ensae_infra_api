from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

env = os.getenv("ENV")
db_address = os.getenv(f"{env}_DB_ADDRESS")
db_port = os.getenv(f"{env}_DB_PORT")
db_name = os.getenv(f"{env}_DB_NAME")


# Replace the placeholder with your Atlas connection string
uri = f"mongodb://{db_address}:{db_port}"

# Create a new client and connect to the server
client = MongoClient(uri)

MARMYTHON_DB = client.get_database(f"{db_name}")