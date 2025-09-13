from pymongo import MongoClient

# Replace the connection string with your MongoDB URI
# For a local MongoDB instance, this is usually "mongodb://localhost:27017/"
MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI)
    db = client.course_selling_api

    # The ping command is a quick and simple way to check if the connection is successful
    client.admin.command('ping')
    print("🎉 Successfully connected to MongoDB!")

except Exception as e:
    print(f"❌ Could not connect to MongoDB: {e}")