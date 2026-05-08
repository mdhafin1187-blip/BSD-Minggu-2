import json, os
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client_mongo = MongoClient(os.getenv("MONGO_URI"))
db = client_mongo[os.getenv("DB_NAME")]
collection = db["sensor"]

TOPIC = "test/dhafin123"

def on_connect(client, userdata, flags, rc, properties=None):
    print("✅ Connected")
    client.subscribe(TOPIC)
    print("📡 Subscribe ke:", TOPIC)

def on_message(client, userdata, msg):
    print("📥 MASUK:", msg.payload)

    payload = json.loads(msg.payload.decode())
    payload["timestamp"] = datetime.fromisoformat(payload["timestamp"])

    collection.insert_one(payload)

    print(f"💾 Mongo: {payload['mesin']} | {payload['suhu']}°C")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

print("⏳ Menunggu data...")
client.loop_forever()