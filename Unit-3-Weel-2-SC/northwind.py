# ### Part 2 - The Northwind Database

# Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.
import sqlite3
connection = sqlite3.connect('northwind_small.sqlite3')
cursor = connection.cursor()
print("CURSOR", cursor)

# ![Northwind Entity-Relationship Diagram](./northwind_erd.png)

# Above is an entity-relationship diagram - a picture summarizing the schema and
# relationships in the database. Note that it was generated using Microsoft
# Access, and some of the specific table/field names are different in the provided
# data. You can see all the tables available to SQLite as follows:

# ```python
# >> > cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
# [('Category',), ('Customer',), ('CustomerCustomerDemo',),
#  ('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
#  ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
#  ('Territory',)]
# ```

# *Warning*: unlike the diagram, the tables in SQLite are singular and not plural
# (do not end in `s`). And you can see the schema(`CREATE TABLE` statement)
# behind any given table with:
# ```python
# >> > cursor.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
# [('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
#                               "CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
#                               "ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
#                               VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
#                               VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
#                               NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
# ```

# In particular note that the * primary * key is `Id`, and not `CustomerId`. On
# other tables(where it is a * foreign * key) it will be `CustomerId`. Also note -
# the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
# particular table, but it's a good lesson in the danger of keyword conflicts.

# Answer the following questions(each is from a single table):

# - What are the ten most expensive items(per unit price) in the database?
# query = "SELECT COUNT (*) FROM charactercreator_character;"
# character_total = cursor.execute(query).fetchall()
# print("character_total", character_total)

query = """
SELECT ProductName, UnitPrice FROM Product
ORDER BY UnitPrice DESC LIMIT 10;
"""
exp_items = cursor.execute(query).fetchall()
print("10_exp_items", exp_items)

# - What is the average age of an employee at the time of their hiring? 
# (Hint: a lot of arithmetic works with dates.)
query = """
SELECT AVG(HireDate) -AVG(BirthDate) as avg_hiring_age FROM Employee
"""
avg_age = cursor.execute(query).fetchall()
print("avg_age", avg_age)


# - (*Stretch*) How does the average age of employee at hire vary by city?

# Your code(to load and query the data) should be saved in `northwind.py`, and
# added to the repository. Do your best to answer in purely SQL, but if necessary
# use Python/other logic to help.


### Part 3 - Sailing the Northwind Seas

# You've answered some basic questions from the Northwind database, looking at
# individual tables - now it's time to put things together, and `JOIN`!

# Using `sqlite3` in `northwind.py`, answer the following:

# - What are the ten most expensive items(per unit price) in the database * and*
# their suppliers?
query1 = """
SELECT * FROM Product
LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC LIMIT 10;
"""
exp_items_suppliers = cursor.execute(query1).fetchall()
print("10_exp_items_and_suppliers", exp_items_suppliers)

# - What is the largest category(by number of unique products in it)?
query1 = """
SELECT * FROM Category
LEFT JOIN Product ON Category.Id = Product.CategoryId
ORDER BY CategoryName DESC;
"""
#This is not finished, ran out of time!!

largest_category = cursor.execute(query1).fetchall()
print("largest_category", largest_category)

# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
# (not name, region, or other fields) as the unique identifier for territories.

