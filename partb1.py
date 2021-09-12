# Part B Task 1

import re
import pandas as pd
import numpy as np
import os
import string


# Array to store data in
DataArray = []

# Iterates through all files in cricket directory
for i in os.listdir("cricket"):
    
    # stops it from erroring on non .txt
    if '.txt' in i:

        # makes path location of file
        text_location = 'cricket/' + i

        # opens text file
        with open(text_location, 'r') as file:
            text = file.read()

            # Regex expression for document ID
            match = re.search(r'\D{4}-\d{3}[A-Z]?', text)
            
        # Appends data to DataArray
        DataArray.append([i, match.group()])


# Converts to nupmy Array
numpyArray = np.array(DataArray)

# turns numpy Array to dataframe with headings, and sorts by filename
df = pd.DataFrame(data=numpyArray, columns=["filename", 'documentID'])
df = df.sort_values(by = ['filename'])

# exports to CSV
df.to_csv('partb1.csv', index = False)
