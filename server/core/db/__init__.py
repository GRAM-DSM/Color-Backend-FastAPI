from pymongo import MongoClient

from server.config import MONGODB_IP, MONGODB_PORT, MONGODB_USERNAME, MONGODB_PASSWORD

client = MongoClient(MONGODB_IP, MONGODB_PORT, username=MONGODB_USERNAME, password=MONGODB_PASSWORD)
