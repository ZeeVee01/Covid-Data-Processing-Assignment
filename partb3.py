# Part B Task 3

import string
import re
import sys
import pandas as pd
import nltk
import os


# Preprocessing function
def preprocessing(text):
    # Step 1
    text = re.sub(r'\d+', '', text)  # Removes numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Removes punctuation

    # Step 2
    text = re.sub(r'\s+', ' ', text)  # Removes tabs, newlines and double spaces

    # Step 3
    text = text.lower()  # text to lower

    return text


# Takes args into keyword array
numkeywords = len(sys.argv)
keywords = []
for i in range(1,numkeywords):
    keywords.append(sys.argv[i])

# buffers keywords with blank space so only full words are covered
i = 0
for keyword in keywords:
    keyword = ' ' + keyword + ' '
    keywords[i] = keyword
    i += 1


for i in os.listdir("cricket"):
    
    # stops it from erroring on non .txt
    if '.txt' in i:
        
        match = 1

        # makes path location of file
        text_location = 'cricket/' + i

        # opens text file
        with open(text_location, 'r') as file:
            text_file = file.read()

            # Regex expression to get document ID
            docID = re.search(r'\D{4}-\d{3}[A-Z]?', text_file)
            
            # Preproccesses text
            text_file = preprocessing(text_file)

            # checks for all matchs and prints if true
            for keyword in keywords:
                if keyword not in text_file:
                    match = 0

            if match:
                print(docID.group())




