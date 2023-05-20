from re import L
import sqlite3
import random
import itertools
from flask import Flask, session, render_template, request, g

## This actually houses the 'app' using Flask to pull data into the html - makes the html more dynamic ##

# Creates the app(?)
app = Flask(__name__)
app.secret_key = "zcoxie rsdkfjepo"

# Sets the initial page
@app.route("/")
def index():
    # This function renders the landing page
    # Input: none
    # Output: render index.html
    
    # Save some columns and use it to create landing html page - passing in relevant data for html
    global name_data, columns, ordered_name_data, route_data
    name_data, columns, ordered_name_data, route_data = get_db()    # Arrays of varying lengths
    return render_template('index.html', name_data = ordered_name_data, route_data = route_data, zip = zip)

# Sets the lookup page
@app.route("/search", methods = ["POST"])
def search():
    # This function renders the search page
    # Input: none
    # Output: render search.html

    # Enter the database and query for the specific pokemon
    db = g._database = sqlite3.connect('pokemon.db')
    c = db.cursor()

    if request.form["search_name"] != "":
        c.execute('SELECT * from pokedata WHERE Name="' + request.form["search_name"] + '" AND Location LIKE "%' + request.form["search_route"] + '%"')
    else:
        c.execute('SELECT * from pokedata WHERE Name LIKE "%' + request.form["search_name"] + '%" AND Location LIKE "%' + request.form["search_route"] + '%"')
    
    all_data = c.fetchall()     # Array of tuples
    
    # If no results found, render a version of index.html, otherwise render search.html
    if len(all_data) > 0:
        return render_template('search.html', name_data = ordered_name_data, route_data = route_data, all_data = all_data, columns = columns, zip = zip)
    else:
        return render_template('index.html', flag = "empty", name_data = ordered_name_data, route_data = route_data, columns = columns, zip = zip)

# Sets the pokedex page
@app.route("/pokedex", methods = ["POST"])
def pokedex():
    # This function renders your personal pokedex
    # Input: none
    # Output: render pokedex.html

    # Enter the database 
    db = g._database = sqlite3.connect('pokemon.db')
    c = db.cursor()

    # Query for the pokedex number data to display
    c.execute('SELECT Number from pokedata')
    number_data = c.fetchall()
    number_data = [val[0] for val in number_data]

    # Query for the sprite to display
    c.execute('SELECT Sprite from pokedata')
    sprite_data = c.fetchall()
    sprite_data = [val[0] for val in sprite_data]

    return render_template('pokedex.html', name_data = name_data, route_data = route_data, sprite_data = sprite_data, number_data = number_data)

# Gather's some constants
def get_db():
    # This function queries the database to gather some values
    # Input: none
    # Output: name_data = Array, columns = Array, ordered_name_data = Array, route_data = Array
    
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('pokemon.db')
        c = db.cursor()
        c.execute("SELECT Name from pokedata")
        name_data = c.fetchall()
        name_data = [val[0] for val in name_data]
        ordered_name_data = name_data.copy()
        ordered_name_data.sort()
        
        route_data = ["Route 1",
        "Route 2",
        "Route 3",
        "Route 4",
        "Route 5",
        "Route 6",
        "Route 7",
        "Route 8",
        "Route 9",
        "Route 10",
        "Route 11",
        "Route 12",
        "Route 13",
        "Route 14",
        "Route 15",
        "Route 16",
        "Route 17",
        "Route 18",
        "Route 19",
        "Route 20",
        "Route 21",
        "Route 22",
        "Route 23",
        "Route 24",
        "Route 25",
        "Route 26",
        "Route 27",
        "Route 28",
        "Berry Forest",
        "Bond Bridge",
        "Canyon Entrance",
        "Cape Brink",
        "Celadon City",
        "Cerulean Cave",
        "Cerulean City",
        "Cinnabar Island",
        "Diglett Cave",
        "Dotted Hole",
        "Five Island",
        "Five Isle Meadow",
        "Four Island",
        "Fuchsia City",
        "Green Path",
        "Icefall Cave",
        "Indigo Plateau",
        "Kindle Road",
        "Lavender Town",
        "Lost Cave",
        "Memorial Pillar",
        "Mt. Ember",
        "Mt. Moon",
        "Navel Rock",
        "One Island",
        "Outcast Island",
        "Pallet Town",
        "Pattern Bush",
        "Pewter City",
        "Pokémon Mansion",
        "Pokémon Tower",
        "Power Plant",
        "Resort Gorgeous",
        "Roaming Kanto",
        "Rock Tunnel",
        "Rocket Hideout",
        "Rocket Warehouse",
        "Ruin Valley",
        "Safari Zone",
        "Saffron City",
        "Seafoam Islands",
        "Sevault Canyon",
        "Seven Island",
        "Silph Co.",
        "Six Island",
        "SS Anne",
        "Tanoby Ruins",
        "Three Island",
        "Three Isle Path",
        "Three Isle Port",
        "Tohjo Falls",
        "Trainer Tower",
        "Treasure Beach",
        "Two Island",
        "Underground Path 5-6",
        "Underground Path 7-8",
        "Vermilion City",
        "Victory Road",
        "Viridian City",
        "Viridian Forest",
        "Water Labyrinth",
        "Water Path"]

        c.execute("PRAGMA table_info(pokedata);")
        columns = c.fetchall()
        columns = [val[1].replace('_', ' ') for val in columns]
    return name_data, columns, ordered_name_data, route_data

# Closes the app
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Only run this file if it is run directly and not via another script
if __name__ == '__main__':
    app.run()
