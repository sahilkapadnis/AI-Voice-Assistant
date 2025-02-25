from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ai_assistant"]
collection = db["interactions"]

def save_interaction(user_input, response):
    collection.insert_one({"user_input": user_input, "response": response})
