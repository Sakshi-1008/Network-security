
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://psakshi1206_db_user:Admin1234@cluster0.kogwy7v.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)