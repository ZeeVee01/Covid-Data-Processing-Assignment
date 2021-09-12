# Part B Task 2

import string
import re
import os
import sys

# takes arg as path
path = sys.argv[1]

# Create file path
filePath = path[:7] + '/' + path[7:]

with open(filePath, 'r') as file:
    text = file.read()

    # Step 1
    text = re.sub(r'\d+', '', text)  # Removes numbers
    text = text.translate(str.maketrans('', '', string.punctuation)) # Removes punctuation

    # Step 2
    text = re.sub(r'\s+', ' ', text) # Removes tabs, newlines and double spaces

    # Step 3
    text = text.lower() # text to lower

    # prints
    print(text)




