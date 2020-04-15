import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
from sqlalchemy import create_engine

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
URL = os.getenv('URL')

#DB_FILEPATH = ('charactercreator_character_inventory.csv')
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)
cursor = connection.cursor()


titanic_filepath = 'titanic.csv'
df = pd.read_csv(titanic_filepath)

engine = create_engine(URL)
df.to_sql('titanic', engine)
connection = engine.raw_connection()
connection.commit()


