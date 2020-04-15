import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # > loads contents of the .env file into the script's environment

### Connect to ElephantSQL-hosted PostgreSQL
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print(type(connection))

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()

### An example query
cursor.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
# first_results = cursor.fetchone()
# print(first_results)

print('-----------------------')
all_results = cursor.fetchall()
print(all_results)
