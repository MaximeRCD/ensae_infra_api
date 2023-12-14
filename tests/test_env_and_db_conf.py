from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def test_env_conf():
    env = os.getenv("ENV")
    assert env in ["DEV", "STAGING"]

    

def test_db_conf():
    env = os.getenv("ENV")
    db_address = os.getenv(f"{env}_DB_ADDRESS")
    db_port = os.getenv(f"{env}_DB_PORT")
    db_name = os.getenv(f"{env}_DB_NAME")
    uri = f"mongodb://{db_address}:{db_port}"
    client = MongoClient(uri)
    MARMYTHON_DB = client.get_database(f"{db_name}")
    
    assert MARMYTHON_DB.list_collection_names() != []