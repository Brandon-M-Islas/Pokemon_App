## Description ##

# Webscrape to gather information about the base stats in Gen 3 Kanto from various sources and save it 
# into the Statistics table in the database
# All references to data within the Statistics table should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import requests                 # To make api requests
from   bs4 import BeautifulSoup # To pull data from websites
import sqlf                     # To create the database 
import numpy as np              # To handle arrays

#_______________________________________________________________________________________________________#

## Variables ##

# Define Static Variables:
link = "https://pokemondb.net/pokedex/stats/gen1"    # type: str
Nums = np.char.zfill(list(map(str, list(range(1,152)))), 3) 

#_______________________________________________________________________________________________________#

## Main ##

# Gather all of the relevant data from the page

# Travel to the link
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

# Save the table on page and remove the header
tables = soup.findAll('table', {'id': 'pokedex'})
rows = tables[0].select('tbody')[0].select('tr')
rows.pop(0)

# Despite gen=3 parameter, no filter applied. Must select gen 3 abilities
Statistics = []
idx = 0

for row in rows:
    ID    = int(Nums[idx])
    print(type(ID))
    Total = row.select('td')[3]
    HP    = row.select('td')[4]
    ATT   = row.select('td')[5]
    DEF   = row.select('td')[6]
    SPATT = row.select('td')[7]
    SPDEF = row.select('td')[8]
    SPD   = row.select('td')[9]
    Statistics.append((ID, HP, ATT, DEF, SPATT, SPDEF, SPD, Total))
    idx += 1

# Add this to the Abilities table
sqlf.add_many("Statistics", Statistics)
