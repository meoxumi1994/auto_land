import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
auto_land_db = client["auto_land_db"]
