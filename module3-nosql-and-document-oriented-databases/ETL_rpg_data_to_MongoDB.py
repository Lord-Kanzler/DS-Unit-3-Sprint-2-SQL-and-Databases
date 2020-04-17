import pymongo
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
sqlite_connection = sqlite3.connect(DB_FILEPATH)
sqlite_cursor = sqlite_connection.cursor()

row_count = 'SELECT COUNT (*) FROM charactercreator_character'
print(sqlite_cursor.execute(row_count).fetchall())

get_characters = 'SELECT * FROM charactercreator_character'
characters = sqlite_cursor.execute(get_characters).fetchall()

# mongodb+srv: // Lord-Kanzler: < password > @cluster0-arnec.mongodb.net/test?retryWrites = true & w = majority
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database  # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.characters_test  # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

rpg_character = (1, "King Bob", 10, 3, 0, 0, 0, 0, 0)

rpg_doc = {
    'sql_key' : [0],
    'name': characters[1],
    'level': characters[2],
    'exp': characters[3],
    'hp': characters[4],
    'strength': characters[5],
    'intelligence': characters[6],
    'dexterity': characters[7],
    'wisdom': characters[8],
}

collection.insert_one(rpg_doc)

print(type(rpg_character))
print(type(characters))
print(characters)
# Assignment

# Insert values
for character in characters:
    collection.insert_one(characters)


