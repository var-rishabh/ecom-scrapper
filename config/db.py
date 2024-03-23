from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


# connect to the mongo database
def connect_to_mongo():
    # client = MongoClient("mongodb://mongodb:27017/")
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ecomScrapper"]

    return db
