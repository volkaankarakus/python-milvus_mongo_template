from pymilvus import connections as milvus_connections
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# MongoDB bağlantı dizesini .env dosyasından oku
MONGO_DB_CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')

# MILVUS
def get_milvus_connection():
    # Milvus bağlantısını yapılandır
    milvus_connections.connect("default", host="milvus_host", port="milvus_port")
    return milvus_connections.get_connection("default")


# MONGO 
def get_mongo_client():
    # MongoDB bağlantısını yapılandır
    client = MongoClient(MONGO_DB_CONNECTION_STRING)
    return client

def get_mongo_database(client, database_name):
    # Belirli bir veritabanını al
    return client[database_name]

def get_mongo_collection(database, collection_name):
    # Belirli bir koleksiyonu al
    return database[collection_name]