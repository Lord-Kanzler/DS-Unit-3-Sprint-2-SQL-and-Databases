import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()
print("CURSOR", cursor)


# How many total Characters are there?
query = "SELECT COUNT (*) FROM charactercreator_character;"
character_total = cursor.execute(query).fetchall()
print("character_total", character_total)

# How many of each specific subclass?
query2 = "SELECT COUNT (*) FROM charactercreator_cleric;"
cleric = cursor.execute(query2).fetchall()
print("cleric", cleric)

query3 = "SELECT COUNT (*) FROM charactercreator_fighter;"
fighter = cursor.execute(query3).fetchall()
print("fighter", fighter)

query4 = "SELECT COUNT (*) FROM charactercreator_mage;"
mage = cursor.execute(query4).fetchall()
print("mage", mage)

query5 = "SELECT COUNT (*) FROM charactercreator_necromancer;"
necromancer = cursor.execute(query5).fetchall()
print("necromancer", necromancer)

query6 = "SELECT COUNT (*) FROM charactercreator_thief;"
thief = cursor.execute(query6).fetchall()
print("thief", thief)

# How many total Items?
query7 = "SELECT COUNT (*) FROM armory_item;"
item_total = cursor.execute(query7).fetchall()
print("item_total", item_total)

# How many of the Items are weapons? How many are not?
query7 = "SELECT COUNT (*) FROM armory_weapon;"
weapons = cursor.execute(query7).fetchall()
print("weapons", weapons)
print("non weapon", 174 - 37)

# How many Items does each character have? (Return first 20 rows)
query8 = """select
c.character_id
, c."name" as character_name
, count(distinct inv.item_id) as item_count
FROM charactercreator_character c
left join charactercreator_character_inventory inv
on c.character_id = inv.character_id
group by 1, 2 limit 20"""
items_per_char = cursor.execute(query8).fetchall()
print("Items per character", items_per_char)

# How many Weapons does each character have? (Return first 20 rows)
query9 = """
"""

# On average, how many Items does each Character have?
query10 = """select avg(item_count) as avg_items
from (select 
c.character_id
, c."name" as character_name
, count(distinct inv.item_id) as item_count 
FROM charactercreator_character c 
left join charactercreator_character_inventory inv 
on c.character_id = inv.character_id
group by 1, 2
)subq
"""
items_char = cursor.execute(query10).fetchall()
print("Avg.Items per character", items_char)


# On average, how many Weapons does each character have?



##Part 2, Making and populating a Database
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()
print("CURSOR", cursor)

df.to_sql('review', connection, if_exists='replace', index=False)

# Count how many rows you have - it should be 249!
query1 = "SELECT * FROM review;"
rows = cursor.execute(query1).fetchall()
print len(rows)

# How many users who reviewed at least 100 Nature in the category
#  also reviewed at least 100 in the Shopping category?
query2 = """
Select Nature >=100 and Shopping >=100 from review
order by 1 DESC
"""

count = cursor.execute(query2).fetchall()
print("Number of Nature and Shopping >100", count.count((1, )))


# (Stretch) What are the average number of reviews for each category?
