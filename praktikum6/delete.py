from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]

satu_jam_lalu = datetime.utcnow() - timedelta(hours=1)
delete_result = collection.delete_many({"timestamp": {"$lt": satu_jam_lalu}})
print(f"Delete: {delete_result.deleted_count} dokumen dihapus")