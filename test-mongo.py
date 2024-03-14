from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv('./config/.env')

mongo_pwd = os.getenv("MONGO_PWD")
mongo_name = os.getenv("MONGO_NM")
uri = f"mongodb+srv://MongoRL:{mongo_pwd}@mongobongo.crfgjc0.mongodb.net/?retryWrites=true&w=majority&appName={mongo_name}"

client = MongoClient(uri, server_api=ServerApi('1'))

df = pd.read_csv('./Sample_Data.csv')

data = df.to_dict(orient='records')

MongoBongo_db = client['MongoBongo']

TM2020_RL_collection = MongoBongo_db["TM2020_RL"]

TM2020_RL_collection.insert_many(data)

client.close()

