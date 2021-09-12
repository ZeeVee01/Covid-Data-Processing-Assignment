# Part B Task 4

import string
import re
import sys
import pandas as pd
import nltk
import os

from nltk.stem.porter import *

ps = PorterStemmer()


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
for i in range(1, numkeywords):
    keywords.append(sys.argv[i])

# buffers keywords with blank space so only full words are covered
i = 0
for keyword in keywords:
    keyword = ps.stem(keyword)
    keywords[i] = keyword
    i += 1

for i in os.listdir("cricket"):
    
    # stops it from erroring on non .txt
    if '.txt' in i:

        # assume true
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

        # splits text into array
        textsplit = text_file.split(' ')


        # iterates through each keyword
        for keyword in keywords:

            # assumes no match
            curMatch = 0

            # iterates through and checks in stemword against keyword
            for word in textsplit:
                stemword = ps.stem(word)
                if keyword == stemword:
                    curMatch = 1

            # if no match for this keyword, no match overall for this document
            if curMatch != 1:
                match = 0

        if match:
            print(docID.group())
