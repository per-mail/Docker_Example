from pymongo import MongoClient
from pprint import pprint

NONGO_URL = "mongodb://mongo:27017"
client = MongoClient(NONGO_URL)
db = client.admin
dbs_list = db.command("ListDatabases")
pprint(dbs_list)