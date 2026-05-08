import paho.mqtt.client as mqtt
import json
from datetime import datetime
import time
import random

client = mqtt.Client(protocol=mqtt.MQTTv5)
client.connect("broker.hivemq.com", 1883, 60)

mesin_list = ["CNC-01", "CNC-02", "CNC-03", "CNC-04"]

while True:
    data = {
        "mesin": random.choice(mesin_list),                # random mesin
        "suhu": round(random.uniform(60, 100), 2),         # suhu random
        "getaran": round(random.uniform(0.1, 0.5), 2),     # getaran random
        "timestamp": datetime.now().isoformat()
    }

    client.publish("pabrik/sensor/suhu", json.dumps(data))
    print("🚀 Data dikirim:", data)

    time.sleep(2)