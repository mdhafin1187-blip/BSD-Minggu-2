from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]

cursor = collection.find(
    {"mesin": "CNC-01"},
    {"_id": 0, "suhu": 1, "timestamp": 1}
).sort("timestamp", -1).limit(5)
print("Data CNC-01 terbaru:")
for doc in cursor:
    print(doc)

