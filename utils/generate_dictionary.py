# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- #
# Recieves input from modification_types.csv to build a dictionary of modification symbols and short names
# ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- # ---- #

# Importing packages
import pandas as pd
import pprint

# Load the modomics modification csv file (first row is header)
data = pd.read_csv('modification_types.csv', header = 0)

# Create an empty dictionary
dictionary = {}

# For each row in the modomics modification dataframe
for index, row in data.iterrows(): # index refers to row numbers, ignored
    
    # Setting each key and value
    symbol = row['symbol']
    modification = row['modification']

    # If the symbol is in the dictionary, append the corresponding modification to the existing key:value pair
    if symbol in dictionary:
        dictionary[symbol].append(modification)
        
    # If the symbol is not in the dictionary, create a new dictionary entry
    else:
        dictionary[symbol] = [modification]

# Printing the dictionary in a readable format to use for Modomics_Decoder.py
pprint.pprint(dictionary)






