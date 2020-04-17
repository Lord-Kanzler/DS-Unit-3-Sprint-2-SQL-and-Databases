### Part 1 - Making and populating a Database

# Consider the following data:

# | s | x | y |
# |----- | --- | ---|
# | 'g' | 3 | 9 |
# | 'v' | 5 | 7 |
# | 'f' | 8 | 7 |

# Using the standard `sqlite3` module:
import sqlite3

# - Open a connection to a new(blank) database file `demo_data.sqlite3`
connection = sqlite3.connect('demo_data.sqlite3')

# - Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
# the above data(name the table `demo`)
cursor = connection.cursor()
print("CURSOR", cursor)


# - Write and execute appropriate `INSERT INTO` statements to add the data(as
#  shown above) to the database
table_demo = '''
CREATE TABLE demo (
    id PRIMARY KEY,
    s VARCHAR(20) UNIQUE NOT NULL,
    x INT,
    y INT
);
'''
cursor.execute(table_demo)
connection.commit()


insert_demo = '''
INSERT INTO demo
    (s, x, y) 
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
'''
cursor.execute(insert_demo).fetchall()
connection.commit()


# Make sure to `commit()` so your data is saved! The file size should be non-zero.

# Then write the following queries(also with `sqlite3`) to test:

# - Count how many rows you have - it should be 3!
rows = "SELECT COUNT (*) FROM demo;"
rows = cursor.execute(rows).fetchall()
print("rows", rows)

# - How many rows are there where both `x` and `y` are at least 5?
rows_bigger_5 = """SELECT x >= 5 and y >= 5 from demo
order by 1 DESC;"""
rows_bigger_5 = cursor.execute(rows_bigger_5).fetchall()
print("rows_bigger_5", rows_bigger_5.count((1, )))


# - How many unique values of `y` are there(hint - `COUNT()` can accept a keyword
#                                           `DISTINCT`)?
unique_values = "SELECT COUNT (DISTINCT y) FROM demo;"
unique_values = cursor.execute(unique_values).fetchall()
print("unique_values", unique_values)
