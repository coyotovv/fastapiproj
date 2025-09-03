from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "course_selling_platform"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]