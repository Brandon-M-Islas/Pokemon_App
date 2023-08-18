## Description ##

# Webscrape to gather information about the typing advantages in Gen 3 Kanto from various sources and 
# save it into the Advantage table in the database
# All references to data within the Advantage table should be directed here

#_______________________________________________________________________________________________________#

## Imports ##

import numpy as np              # To handle arrays
import sqlf                     # To create the database 

#_______________________________________________________________________________________________________#

## Variables ##

# Define Static Variables:

# Advantage values per type
Non = [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1]
Nor = [1,   1,   1,   1,   1, 0.5,   1,   0, 0.5,   1,   1,   1,   1,   1,   1,   1,   1,   1]
Fig = [2,   1, 0.5, 0.5,   1,   2, 0.5,   0,   2,   1,   1,   1,   1, 0.5,   2,   1,   2, 0.5]
Fly = [1,   2,   1,   1,   1, 0.5,   2,   1, 0.5,   1,   1,   2, 0.5,   1,   1,   1,   1,   1]
Poi = [1,   1,   1, 0.5, 0.5, 0.5,   1, 0.5,   0,   1,   1,   2,   1,   1,   1,   1,   1,   2]
Gro = [1,   1,   0,   2,   1,   2, 0.5,   1,   2,   2,   1, 0.5,   2,   1,   1,   1,   1,   1]
Roc = [1, 0.5,   2,   1, 0.5,   1,   2,   1, 0.5,   2,   1,   1,   1,   1,   2,   1,   1,   1]
Bug = [1, 0.5, 0.5, 0.5,   1,   1,   1, 0.5, 0.5, 0.5,   1,   2,   1,   2,   1,   1,   2, 0.5]
Gho = [0,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   1,   2,   1,   1, 0.5,   1]
Ste = [1,   1,   1,   1,   1,   2,   1,   1, 0.5, 0.5, 0.5,   1, 0.5,   1,   2,   1,   1,   2]
Fir = [1,   1,   1,   1,   1, 0.5,   2,   1,   2, 0.5, 0.5,   2,   1,   1,   2, 0.5,   1,   1]
Wat = [1,   1,   1,   1,   2,   2,   1,   1,   1,   2, 0.5, 0.5,   1,   1,   1, 0.5,   1,   1]
Gra = [1,   1, 0.5, 0.5,   2,   2, 0.5,   1, 0.5, 0.5,   2, 0.5,   1,   1,   1, 0.5,   1,   1]
Ele = [1,   1,   2,   1,   0,   1,   1,   1,   1,   1,   2, 0.5, 0.5,   1,   1, 0.5,   1,   1]
Psy = [1,   2,   1,   2,   1,   1,   1,   1, 0.5,   1,   1,   1,   1, 0.5,   1,   1,   0,   1]
Ice = [1,   1,   2,   1,   2,   1,   1,   1, 0.5, 0.5, 0.5,   2,   1,   1, 0.5,   2,   1,   1]
Dra = [1,   1,   1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   1,   1,   1,   2,   1,   0]
Dar = [1, 0.5,   1,   1,   1,   1,   1,   2,   1,   1,   1,   1,   1,   2,   1,   1, 0.5, 0.5]
Fai = [1,   2,   1, 0.5,   1,   1,   1,   1, 0.5, 0.5,   1,   1,   1,   1,   1,   2,   2,   1]

# Dict for name of type and advantage values
Types =    {"Non": Non,
            "Nor": Nor,
            "Fig": Fig,
            "Fly": Fly,
            "Poi": Poi,
            "Gro": Gro,
            "Roc": Roc,
            "Bug": Bug,
            "Gho": Gho,
            "Ste": Ste,
            "Fir": Fir,
            "Wat": Wat,
            "Gra": Gra,
            "Ele": Ele,
            "Psy": Psy,
            "Ice": Ice,
            "Dra": Dra,
            "Dar": Dar,
            "Fai": Fai}

#_______________________________________________________________________________________________________#

## Main ##

# Create empty list to hold tuples
vals = []

# Iterate through every combo of typings - ignoring a Type_1 of Non
for Type_1 in Types.keys():
    if Type_1 != "Non":
        for Type_2 in Types.keys():

            # Multiply advantages to get aggregate advantages
            advs = list(np.multiply(Types[Type_1], Types[Type_2]))
            
            # Put the types at the beginning of the list
            advs.insert(0,Type_2)
            advs.insert(0,Type_1)

            # Add this to the vals list as a tuple
            vals.append(tuple(advs))

# Add this to the Advantage table
sqlf.add_many("Advantage",vals)
