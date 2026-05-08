from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]