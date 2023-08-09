## Description ##

# Houses the sqlite functions that are used in the actual project. 
# All references to data table manipulation should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import sqlite3  # To use Sqlite as datatable

#_______________________________________________________________________________________________________#

## Global Variables ##

DB = "pokemon.db"

#_______________________________________________________________________________________________________#

## Functions ##

# Query the database and return all records
def show_all(table: str):

    # Input: table = name of the table

    # Creates the database if does not exist; connect thereafter
    conn = sqlite3.connect(DB)

    # Create cursor
    c = conn.cursor()

    # Query all items in given table
    c.execute("SELECT * FROM " + table)
    items = c.fetchall()
    for item in items:
        print(item)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add a single record to the database
def add_one(table: str, value: tuple):

    # Input: table = name of the table
    #        value = tuple of every value for the record

    # Creates the database if does not exist; connect thereafter
    conn = sqlite3.connect(DB)

    # Create cursor
    c = conn.cursor()

    # Add one record at a time
    c.execute("INSERT INTO " + table + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", value)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Deletes a table in the database
def delete_table(table: str):

    # Input: table = name of the table

    # Creates the database if does not exist; connect thereafter
    conn = sqlite3.connect(DB)

    # Create cursor
    c = conn.cursor()

    # Delete table
    c.execute("DROP TABLE " + table)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add many new records to the database
def add_many(table: str, List: list):

    # Input: table = name of the table
    #         List = list of tuples with every value for each record

    # Creates the database if does not exist; connect thereafter
    conn = sqlite3.connect(DB)

    # Create cursor
    c = conn.cursor()

    # Iterate through list to add each
    c.executemany("INSERT INTO " + table + " VALUES " + columns(len(List[0])), (List))

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add a table to the database
def create_table(table: str):

    # Input: table = name of the table

    # Creates the database if does not exist; connect thereafter
    conn = sqlite3.connect(DB)

    # Create cursor
    c = conn.cursor()

    # Create a Table
    c.execute("CREATE TABLE " + table + """ (
        Number text,
        Name text,
        Typing text,
        Abilities text,
        Gender text,
        Species text, 
        Height text, 
        Weight text,
        Item text, 
        Pokedex text, 
        Egg_Group text,
        Egg_Steps text,
        EV_Yield text,
        Catch_Rate text,
        Growth_Rate text, 
        Base_Friendship text,
        Location text,
        Sprite,
        Shiny_Sprite,
        Typing_Img text,
        Item_Img)""")

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# defines the number of columns for the table; (?, ?, ..., ?)
def columns(l: int):

    # Input: l = length of the tuple

    # Start the tuple
    text = "("

    # Add ? for each item in the list
    for i in range(0,l):
        if i == 0:
            text = text + "?"
        else:
            text = text + ", ?"

    # Close the tuple
    text = text + ")"

    # Return the tuple 
    return text
