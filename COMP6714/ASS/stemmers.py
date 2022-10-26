import json
import sys
import nltk
import regex
from sys import stdin
from myparser import SimpleBooleanParser
import spacy
index = None
import en_core_web_sm
nlp = en_core_web_sm.load()
def normalise(tokens):
    tokens = [tk.lower() for tk in tokens]
    return tokens

def stem(tokens):
    porter = nltk.LancasterStemmer()
    return [porter.stem(tk) for tk in tokens]

if __name__ == '__main__':
    for line in stdin:
        # Get rid of end of line
        query = line[:-1]    
        query = query.lower()
        data = nlp(query)
        for i in data:
            print(i.lemma_)
        # print(len(result))
