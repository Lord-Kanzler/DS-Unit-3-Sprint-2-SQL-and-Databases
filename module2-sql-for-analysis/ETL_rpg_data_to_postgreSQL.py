from psycopg2.extras import execute_values
import psycopg2
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import os

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
URL = os.getenv('URL')

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
sqlite_connection = sqlite3.connect(DB_FILEPATH)
sqlite_cursor = sqlite_connection.cursor()

row_count = 'SELECT COUNT (*) FROM charactercreator_character'
print(sqlite_cursor.execute(row_count).fetchall())

get_characters = 'SELECT * FROM charactercreator_character'
characters = sqlite_cursor.execute(get_characters).fetchall()


#rpg schema
print(sqlite_cursor.execute('PRAGMA table_info(charactercreator_character);').fetchall())

#pg part
create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""
pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION:', pg_connection)
pg_cursor = pg_connection.cursor()

pg_cursor.execute(create_character_table)
pg_connection.commit()

# Insert values
for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level,exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(characters[0][1:]) + ";"
    pg_cursor.execute(insert_character)
pg_connection.commit()
