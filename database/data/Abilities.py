## Description ##

# Webscrape to gather information about the abilities in Gen 3 Kanto from various sources and save it 
# into the Abilities table in the database
# All references to data within the Abilities table should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import requests                 # To make api requests
from   bs4 import BeautifulSoup # To pull data from websites
import sqlf                     # To create the database 

#_______________________________________________________________________________________________________#

## Variables ##

# Define Static Variables:
link = "https://pokemondb.net/ability#gen=3"    # type: str

#_______________________________________________________________________________________________________#

## Main ##

# Gather all of the relevant data from the page

# Travel to the link
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

# Save the table on page and remove the header
tables = soup.findAll('table', {'id': 'abilities'})
rows = tables[0].select('tr')
rows.pop(0)

# Despite gen=3 parameter, no filter applied. Must select gen 3 abilities
Abilities = [(row.select('td')[0].text, row.select('td')[2].text) for row in rows if row.select('td')[3].text == "3"]

# Add this to the Abilities table
sqlf.add_many("Abilities", Abilities)
