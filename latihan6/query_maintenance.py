import pandas as pd
from pymongo import MongoClient

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["latihan6"]
collection = db["maintenance"]

# =========================
# 1. Query biaya > 1.000.000
# =========================
result = list(collection.find(
    {"biaya": {"$gt": 1000000}},
    {"_id": 0}
))

df = pd.DataFrame(result)

print("=== Data biaya > 1.000.000 ===")
print(df)


# =========================
# 2. Update data
# =========================
update_result = collection.update_one(
    {"mesin": "CNC-01", "biaya": 1200000},
    {"$set": {"teknisi": "Dewi"}}
)

print("\n=== Update ===")
print("Matched:", update_result.matched_count)
print("Modified:", update_result.modified_count)


# =========================
# 3. Aggregation total biaya per bulan
# =========================
pipeline = [
    {
        "$project": {
            "bulan": {
                "$dateToString": {
                    "format": "%Y-%m",
                    "date": "$tanggal"
                }
            },
            "biaya": 1
        }
    },
    {
        "$group": {
            "_id": "$bulan",
            "total_biaya": {"$sum": "$biaya"}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]

agg_result = list(collection.aggregate(pipeline))

df_agg = pd.DataFrame(agg_result)

if not df_agg.empty:
    df_agg.rename(columns={"_id": "bulan"}, inplace=True)

print("\n=== Total biaya per bulan ===")
print(df_agg)