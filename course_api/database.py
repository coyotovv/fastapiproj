from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI)
    db = client.course_selling_api


    client.admin.command('ping')
    print("🎉 Successfully connected to MongoDB!")

except Exception as e:
    print(f"❌ Could not connect to MongoDB: {e}")