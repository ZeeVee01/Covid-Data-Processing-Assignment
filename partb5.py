## Part B Task 5

import string
import re
import os
import sys
import pandas as pd
import nltk
import sklearn
import math
from numpy import dot
from numpy.linalg import norm

from sklearn.feature_extraction.text import TfidfTransformer
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

def cosine_sim(v1, v2):
    return dot(v1, v2)/(norm(v1)*norm(v2))


# Takes args into keyword array
numkeywords = len(sys.argv)
keywords = []
for i in range(1, numkeywords):
    keywords.append(sys.argv[i])

# buffers keywords with blank space so only full words are covered
numKeywords = 0
for keyword in keywords:
    keyword = ps.stem(keyword)
    keywords[numKeywords] = keyword
    numKeywords += 1
    
term_counts = []
docIDarr = []
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


        documentTermCount = []
        # iterates through each keyword
        for keyword in keywords:
            wordcount = 0

            # assumes no match
            curMatch = 0

            # iterates through and checks in stemword against keyword
            for word in textsplit:
                stemword = ps.stem(word)
                if keyword == stemword:
                    curMatch = 1
                    wordcount += 1


            # if no match for this keyword, no match overall for this document
            if curMatch != 1:
                match = 0
                
            documentTermCount.append(wordcount)
        
        # if document is not considered a match set all values to 0
        j = 0
        if match == 0:
            for count in documentTermCount:
                documentTermCount[j] = 0
                j += 1
                
        term_counts.append(documentTermCount)  
        docIDarr.append(docID.group())
        
        
# makes tfidf array from term_counts and stores in doc_tfidf      
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(term_counts)
transformer.idf_
doc_tfidf = tfidf.toarray()
    
# makes unit vector
q_unit = []
for j in range(0, numKeywords):
    q_unit.append(1/(math.sqrt(numKeywords)))
    
# calculates the cosine values
sims = []
for d_id in range(doc_tfidf.shape[0]):
    if doc_tfidf[d_id][0] == 0:
        sims.append(0)
    else:
        sims.append(cosine_sim(q_unit, doc_tfidf[d_id]))


# prints cosine values that are not 0
print("documentID score")
i = 0
for score in sims:
    if score > 0.0:
        print(docIDarr[i].ljust(9, ' '), "{:.4f}".format(score))
    i += 1

    
    

            
        

    

