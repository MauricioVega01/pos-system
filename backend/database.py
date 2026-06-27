from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["pos_system"]

products_collection = db["products"]
sales_collection = db["sales"]