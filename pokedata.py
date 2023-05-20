## Description ##

# Webscrape to gather information about the og 151 pokemon from various sources and save it into a database
#   All references to data within the datatbale should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import numpy as np                      # To handle arrays
import requests                         # To make api requests
from bs4 import BeautifulSoup           # To pull data from websites
import re                               # To use regular expressions
import sqlite3                          # To connect to database and make 1-off changes
import sqlf                             # To create the database 

# from tokenize import Name, Number       # Unused

#_______________________________________________________________________________________________________#

## Variables ##

# Define Static Variables:
#   all of type List[str]
Number_Entries        = np.char.zfill(list(map(str, list(range(1,152)))), 3)                                       # numbers 001-151
links                 = ["https://www.serebii.net/pokedex-rs/" + num + ".shtml" for num in Number_Entries]       # links to every pokemon page
Sprite_Link           = ["https://www.serebii.net/red_green/pokemon/" + num + ".gif" for num in Number_Entries]  # links to every pokemon sprite
Shiny_Link            = ["https://www.serebii.net/Shiny/FRLG/" + num + ".png" for num in Number_Entries]         # links to every pokemon shiny sprite

# Create variables that will hold data from each page: 
#   Most of type List[str]
#   Catch rate of type List[int]
#   All data of type List[tuple]
Name_Entries          = []  # name
Typing_Entries        = []  # type(s)
Typing_Img_Entries    = []  # type image(s)
Height_Entries        = []  # height
Species_Entries       = []  # species
Weight_Entries        = []  # weight
Abilities_Entries     = []  # ability/abilities
Abilities_Inf_Entries = []  # ability description(s)
Item_Entries          = []  # item chance(s)
ItemImage_Link        = []  # item image(s)
Pokedex_Entries       = []  # pokedex entry
EV_Entries            = []  # ev yield
Catch_Entries         = []  # catch rate
Gender_Entries        = []  # gender distribution
Egg_Cycle_Entries     = []  # egg cycle
Egg_Group_Entries     = []  # egg group
Growth_Entries        = []  # growth speed
Friendship_Entries    = []  # base friendship
Route_Entries         = []  # locations
All_Data              = []  # all above data

# Temporarily unused variables
#   All of type List[int]
HP_Entries            = []  # Base HP
Attack_Entries        = []  # Base ATK
Defense_Entries       = []  # Base DEF
SpAttack_Entries      = []  # Base SPA
SpDefense_Entries     = []  # Base SPD
Speed_Entries         = []  # Base SP

#_______________________________________________________________________________________________________#

## Functions ##

# Gather all of the relevant data from a particular page
def data_scrape_serebii(link):
    # Travel to the link
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Save all the tables on page
    tables = soup.findAll('table', {'class': 'dextable'})

    # Select info from the first table
    info = tables[0]

    ## Simple Data Collection ##

    # Get the name, species, height, and weight
    Name_Entries.append(info.select('tr')[1].select('td')[5].text.replace('\n','').replace('\t',''))
    Species_Entries.append(info.select('tr')[10].select('td')[0].text.replace('\n','').replace('\t',''))
    Height_Entries.append(info.select('tr')[10].select('td')[3].text.replace('\n','').replace('\t',''))
    Weight_Entries.append(info.select('tr')[10].select('td')[4].text.replace('\n','').replace('\t',''))
    
    ## Data Collection with Caveats ##
 
    # Get the ability/abilities
    #   Handle cases where pokemon has 2 abilities

    # Save the single ability or save the 2 abilities in a list
    if '&' not in info.select('tr')[3].select('b')[2].text.replace('Ability: ',''):
        Abilities_Entries.append(info.select('tr')[3].select('b')[2].text.replace('Ability: ',''))
    else:
        a = info.select('tr')[3].select('b')[2].text.replace('Ability: ','')
        a1 = a.replace(a[a.find('&')-1:],'')
        a2 = a.replace(a[:a.find('&')+2],'')
        Abilities_Entries.append([a1, a2])

    # If there are 2 abilities then get information for 2 abilities, otherwise save the 1
    if len(Abilities_Entries[-1]) == 2:
        a = info.select('tr')[5].select('td')[0].text.replace('\n','').replace('\t','').replace(Abilities_Entries[-1][0]+': ','')
        a1 = a.replace(a[a.find(Abilities_Entries[-1][1]):],'')
        if a1[-1] == '.':
            a1.replace(a1[-1],'')
        elif a1[-2] == '.':
            a1.replace(a1[-2:],'')
        a2 = a.replace(a[:a.find(":")+2],'')
        if a2[-1] == '.':
            a2.replace(a2[-1],'')
        Abilities_Inf_Entries.append([a1, a2])
    else:
        a = info.select('tr')[5].select('td')[0].text.replace('\n','').replace('\t','')
        if a[-1] == '.':
            a.replace(a[-1],'')
        elif a[-2] == '.':
            a.replace(a[-2:],'')
        Abilities_Inf_Entries.append(a)

    # Get the gender
    a = info.select('tr')[8].text.replace('\n','').replace('\t','').replace(' %', '%')
    a = a.replace(a[a.find('Female'):],'\n' + a[a.find('Female'):])
    Gender_Entries.append(a)

    # Get the typing
    #   Handle the cases where pokemon has 2 tyings
    
    # Save the single type when the other is "na" or save both
    if 'na' in info.select('tr')[10].select('img')[1].get('src').replace('/pokedex-rs/type/','').replace('.gif',''):
        Typing_Img_Entries.append("https://www.serebii.net/" + info.select('tr')[10].select('img')[0].get('src'))
        Typing_Entries.append(info.select('tr')[10].select('img')[0].get('src').replace('/pokedex-rs/type/','').replace('.gif',''))
    else:
        Typing_Img_Entries.append("https://www.serebii.net/" + info.select('tr')[10].select('img')[0].get('src') + 
                                ", https://www.serebii.net/" + info.select('tr')[10].select('img')[1].get('src'))
        Typing_Entries.append(info.select('tr')[10].select('img')[0].get('src').replace('/pokedex-rs/type/','').replace('.gif','') + 
                            "\n" + info.select('tr')[10].select('img')[1].get('src').replace('/pokedex-rs/type/','').replace('.gif',''))

    # Move to the next table
    info = tables[1]

    # Get the item it may hold in the wild
    #   Handle the cases where there are no item chances for this poekemon in this generation/game
    a = info.select('tr')[1].select('td')[0].text.replace('\n','').replace('\t','')
    a = a[a.find('FRLG')+4:]

    if a.find('%') != len(a)-1:
        a = a.replace(a[a.find('%'):],'%\n' + a[a.find('%')+1:])

    if 'FRLG' in info.select('tr')[1].select('td')[0].text:
        Item_Entries.append(a)
    else: 
        Item_Entries.append("None")

    # Get the image of that item
    if Item_Entries[-1] != "None":
        ItemImage_Link.append("https://www.serebii.net" + info.select('tr')[1].select('td')[0].select('img')[0].get('src'))
    else:
        ItemImage_Link.append("None")
        
    # Move to the next table
    info = tables[3]

    # Get the pokedex entry
    Pokedex_Entries.append(info.select('tr')[4].select('td')[1].text.replace('\n','').replace('\t',''))

    # Move to the next table
    info = tables[4]

    #_______________________________________________________________________________________________________#

    # Get the routes
    #   The route names/formatting are very inconsistent. Some attempts to clean that upon collection  
    a = info.select("tr")[5].select("td")[1].text

    a = re.sub(", &", " &", a)

    while re.search("[A-Za-z ]*[A-Za-z]+ \d+, \d+", a) or re.search("[A-Za-z ]*[A-Za-z]+ \d+ & \d+", a) is not None:
        if re.search("[A-Za-z ]*[A-Za-z]+ \d+, \d+", a) is None:
            b = re.search("[A-Za-z ]*[A-Za-z]+ \d+ & \d+", a).group()
            word = re.search("[A-Za-z ]*[A-Za-z]+ ", b).group()
            nums = re.findall("\d+", b)
            a = re.sub(word+nums[0]+" & "+nums[1], word+nums[0]+" &"+word+nums[1], a)
        else:
            b = re.search("[A-Za-z ]*[A-Za-z]+ \d+, \d+", a).group()
            word = re.search("[A-Za-z ]*[A-Za-z]+ ", b).group()
            nums = re.findall("\d+", b)
            a = re.sub(word+nums[0]+", "+nums[1], word+nums[0]+", "+word+nums[1], a)
    
    text = re.sub("\\s+", " ",a)
    text = re.sub("Routes", "Route", text)
    text = re.sub("Areas", "Area", text)

    Route_Entries.append(text)

    #_______________________________________________________________________________________________________#

    # Move to the next table
    #   Some pokemon have a 'Special Attack' table. Figure out which table to be on based on what the current table is
    if len(tables) < 11: 
        info = tables[7]
        idx = 7
    else:
        info = tables[11]
        idx = 11
        if "Special Attacks" in info.select('tr')[0].text:
            info = tables[12]
            idx = 12
        elif "Egg Groups" in info.select('tr')[0].text:
            info = tables[10]
            idx = 10

    # Get the Egg Cycle, Catch Rate, and EV Yield
    Egg_Cycle_Entries.append(info.select('tr')[1].select('td')[0].text.replace('\n','').replace('\t',''))
    Catch_Entries.append(info.select('tr')[1].select('td')[2].text.replace('\n','').replace('\t',''))

    a = info.select('tr')[1].select('td')[1].text.replace('\n','').replace('\t','')
    if "," in a:
        a = a.replace(', ', '\n')

    EV_Entries.append(a)

    #_______________________________________________________________________________________________________#

    # Move to the bulbapedia page
    # Travel to the link

    if Name_Entries[-1] == 'Nidoran (F)':
        link = "https://bulbapedia.bulbagarden.net/wiki/Nidoran%E2%99%80_(Pok%C3%A9mon)"
    elif Name_Entries[-1] == 'Nidoran (M)': 
        link = "https://bulbapedia.bulbagarden.net/wiki/Nidoran%E2%99%82_(Pok%C3%A9mon)"
    else: 
        link = "https://bulbapedia.bulbagarden.net/wiki/" + re.sub(' ', '_', Name_Entries[-1]) + "_(Pok%C3%A9mon)"

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Save the relevant area
    info = soup.findAll('a', {'title': re.compile('(Egg Group)')})
    
    # Save the egg group(s)
    if len(info) == 2:
        Egg_Group_Entries.append(info[-1].text)
    elif len(info) >= 3:
        Egg_Group_Entries.append(info[1].text + '\n' + info[2].text)
    
    # Save the relevant area
    if soup.find('a', {'title': re.compile('base friendship')}) == None:
        print(Name_Entries[-1])

    info = soup.find('a', {'title': re.compile('base friendship')}).find_next('td').text.replace('\n','')

    # Save the base friendship
    Friendship_Entries.append(info)
   
    # Save the relevant area
    info = soup.findAll('a', {'title': 'Experience'})[1].find_next('td').text.replace('\n','')

    # Save the base friendship
    Growth_Entries.append(info)

#_______________________________________________________________________________________________________#

## We're going to use serebii for gen III (FireRed) Pokemon information

# Now we will loop over every link and gather the data
#   We can also comment out the loop and choose a number if we'd like to test

for num in range(0,len(Number_Entries)):
    data_scrape_serebii(links[num])
    print(Number_Entries[num] + " " + Name_Entries[num] + " successful")
    
# Save the data into usable format for SQLite
#   Loop over every pokemon
for i in range(0,len(Name_Entries)):
    # Do some pre-cleaning by separating the abilities if there are multiple and displaying them appropriately
    if len(Abilities_Entries[i]) == 2:
        try:
            ability = Abilities_Entries[i][0] + ': ' + Abilities_Inf_Entries[i][0] + '\n' + Abilities_Entries[i][1] + ': ' + Abilities_Inf_Entries[i][1]
        except:
            print("It looks like "+Abilities_Entries[i]+" is a problem")
            print("The current i is: " + i)
    else:
        try:
            ability = Abilities_Entries[i] + ': ' + Abilities_Inf_Entries[i]
        except:
            print("It looks like "+Abilities_Entries[i]+" is a problem")
            print("The current i is: " + i)

    # Add a tuple to the list that holds all info about that pokemon
    try:
        All_Data.append((Number_Entries[i], Name_Entries[i], Typing_Entries[i], ability, Gender_Entries[i], Species_Entries[i], Height_Entries[i], Weight_Entries[i], Item_Entries[i], Pokedex_Entries[i], Egg_Group_Entries[i], Egg_Cycle_Entries[i], EV_Entries[i], Catch_Entries[i], Growth_Entries[i], Friendship_Entries[i], Route_Entries[i], Sprite_Link[i], Shiny_Link[i], Typing_Img_Entries[i], ItemImage_Link[i]))
    except IndexError:
        print("This is an index error")
        print("we got here")
        print(i)
        raise Exception("What is causing this now")
        
# Create a database and table
table_name = "Pokedata"
sqlf.create_table(table_name)
try:
    sqlf.add_many(table_name, All_Data)
except:
    sqlf.delete_table(table_name)