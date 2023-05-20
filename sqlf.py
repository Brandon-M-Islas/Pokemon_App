## Description ##

# Houses the sqlite functions that are used in the actual project. 
# All references to data table manipulation should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import sqlite3  # To use Sqlite as datatable

#_______________________________________________________________________________________________________#

## Functions ##

# Query the database and return all records
def show_all(table):

    # Creates the database 'pokemon.db' if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Executes a transaction that may change the database
    c.execute("SELECT * FROM " + table)
    items = c.fetchall()
    for item in items:
        print(item)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add a single record to the database
def add_one(table, value):
    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Create a Table; Executes a transaction that may change the database
    # c.execute("""CREATE TABLE " + pokedata + " (name text)""")

    # Add one record at a time; Executes a transaction that may change the database
    c.execute("INSERT INTO " + table + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", value)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Deletes a table in the database
def delete_table(table):
    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Deelete table; Executes a transaction that may change the database
    c.execute("DROP TABLE " + table)

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add many new records to the database
def add_many(table, List):

    # Creates the database 'customer.db' since if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Iterate through list to add each; Executes a transaction that may change the database
    c.executemany("INSERT INTO " + table + " VALUES " + columns(len(List[0])), (List))

    # Commits any pending transactions to change the database 
    conn.commit()

    # Close connection
    conn.close()

# Add a table to the database
def create_table(table):
    # Creates the database 'pokemon.db' if does not exist; connect thereafter
    conn = sqlite3.connect('pokemon.db')

    # Create cursor
    c = conn.cursor()

    # Create a Table; Executes a transaction that may change the database
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

# defines the number of columns for the table
def columns(l):


    text = "("
    for i in range(0,l):
        if i == 0:
            text = text + "?"
        else:
            text = text + ", ?"

    text = text + ")" 
    return text
