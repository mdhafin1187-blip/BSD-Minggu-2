from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]

update_result = collection.update_many(
    {"suhu": {"$gt": 90}},
    {"$set": {"status": "maintenance"}}
)
print(f"Update: {update_result.modified_count} dokumen diubah")