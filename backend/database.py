from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URL)

db = client[DB_NAME]

products_collection = db["products"]
sales_collection = db["sales"]