from pymongo import MongoClient
from dotenv import load_dotenv
from bson.binary import UuidRepresentation
import os


load_dotenv()
BASE_URL = os.environ.get('MONGO_URL')
BASE_PORT = int(os.environ.get('MONGO_PORT'))
client = MongoClient(BASE_URL, BASE_PORT, uuidRepresentation='standard')
db = client.get_database("db1")