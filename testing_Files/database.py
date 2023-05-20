## Description ##

# Houses example sqlite functions that can be used to troubleshoot datatable manipulation 
# and test new commands 
# Use this to learn how to use sqlite with examples and functions 

#_______________________________________________________________________________________________________#

## Imports ##

import sqlite3   # To use Sqlite as datatable

#_______________________________________________________________________________________________________#


# Creates the database 'customer.db' since if does not exist; connect thereafter
conn = sqlite3.connect('customer.db')

# Create cursor
c = conn.cursor()

# Create a Table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text 
    )""")

# Add one record at a time
c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Tim', 'Smith', 'tim@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'brown@codemy.com')")

# Add many records at a time
# many_customers = [
#                     ('Wes', 'Brown', 'wes@brown.com'), 
#                     ('Steph', 'Kuewa', 'steph@kuewa.com'), 
#                     ('Dan', 'Pas', 'dan@pas.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Print results
# c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall())

# items = c.fetchall()
# print("NAME" + "\t\tEMAIL")
# print("--------" + "\t--------")
# for item in items:
#     print(item[0] + " " + item[1] + "\t" + item[2])

# Include the id
# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)

# Find specific query
# c.execute("SELECT * FROM customers WHERE email LIKE '%codemy%'")
# items = c.fetchall()
# for item in items:
#     print(item)

# Update record
# c.execute("""UPDATE customers SET first_name = 'Bob'
#             WHERE last_name = 'Elder'
#             """)

# # Creates the database 'pokemon.db' if does not exist; connect thereafter
# conn = sqlite3.connect('pokemon.db')

# # Create cursor
# c = conn.cursor()

# c.execute("ALTER TABLE pokedata ADD COLUMN Shiny_Link varchar")

# for i in range(len(Number_Entries)):
#     c.execute("""UPDATE pokedata SET Shiny_Link = '""" + Shiny_Link[i] + """'
#                 WHERE Number = '""" + Number_Entries[i] + """'
#                 """)


#delte a table
# DROP TABLE [IF EXISTS] [schema_name.]table_name;

# # Commit command
# conn.commit()

# # Close connection
# conn.close()


# Creates the database 'pokemon.db' if does not exist; connect thereafter
conn = sqlite3.connect('pokemon.db')

# Create cursor
c = conn.cursor()

# Update record
# c.execute("""UPDATE customers SET first_name = 'Marty'
#             WHERE rowid = 4
#             """)

# Delete record
# c.execute("DELETE from customers WHERE rowid = 6")



# Ordered Query
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
# items = c.fetchall()
# for item in items:
#     print(item)

# AND/OR Query
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%Br%' or rowid = 3")
# items = c.fetchall()
# for item in items:
#     print(item)

# Limit Query
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 3")
# items = c.fetchall()
# for item in items:
#     print(item)

# Delete table
# c.execute("DROP TABLE customers")




# Recieve feedback that it was successful
# print("Command executed successfully...")
# 5 Datatypes:
# NULL
# INTEGER
# REAL 
# TEXT
# BLOB

#_______________________________________________________________________________________________________#

#Query the database and return all records
def show_all():

    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('customer.db')

    # Create cursor
    c = conn.cursor()

    # Include the id
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Add a new record to the database
def add_one(first,last,email):

    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('customer.db')

    # Create cursor
    c = conn.cursor()

    # Add one record at a time
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Delete recrod from database
def delete_one(id):
    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('customer.db')

    # Create cursor
    c = conn.cursor()

    # Delete record
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

# Add a many new records to the database
def add_many(List):

    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('customer.db')

    # Create cursor
    c = conn.cursor()

    # Add one record at a time
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (List))

    # Commit command
    conn.commit()

    # Close connection
    conn.close()

def create_table():
    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Create a Table
    c.execute("""CREATE TABLE pokedata (
            Number int,
            Name text,
            Ability text 
        )""")