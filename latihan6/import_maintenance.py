import pandas as pd
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["latihan6"]
collection = db["maintenance"]

# Baca file CSV
df = pd.read_csv("maintenance.csv", encoding="utf-8")

# Konversi kolom tanggal ke datetime
df["tanggal"] = pd.to_datetime(df["tanggal"])

# Ubah ke list of dictionary
data = df.to_dict(orient="records")

# Insert ke MongoDB
if data:
    collection.insert_many(data)
    print("✅ Data berhasil diimport!")
else:
    print("❌ Data kosong, tidak ada yang diinsert")