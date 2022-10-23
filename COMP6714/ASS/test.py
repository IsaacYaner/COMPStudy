from lib2to3.pgen2.literals import simple_escapes
import sys
import json
import nltk
import regex
from sys import stdin
from myparser import SimpleBooleanParser


def normalise(tokens):
    tokens = [tk.lower() for tk in tokens]
    return tokens

def stem(tokens):
    porter = nltk.PorterStemmer()
    return [porter.stem(tk) for tk in tokens]
    
# Write each operator below
# () > | > +n > /n > +s > /s > &
def echo_expression(dest, src, op):
    return '(' + dest + op + '' + src + ')'

def search_or():
    pass

path_index = sys.argv[1]
index = None
with open(path_index) as f:
    index = f.read()
    index = json.loads(index)

print(index['shower'])

terms = {
'expression':       ['&'],
'in_sentence':      ['/s'],
'after_sentence':   [r'\+s'],
'in_n':             [r'/[0-9]+'],
'after_n':          [r'\+[0-9]+'],
'term':             [r'\|'],
'factor':           [],
'word':             [],
} 
operations = {
'expression':       echo_expression,
'in_sentence':      echo_expression,
'after_sentence':   echo_expression,
'in_n':             echo_expression,
'after_n':          echo_expression,
'term':             echo_expression,
} 
def value(text):
    try: 
        text = normalise([text])
        text = stem(text)
        return index[text[0]]
    except:
        return {}
parser = SimpleBooleanParser(terms, operations, value)

for line in stdin:
    # Get rid of end of line
    query = line[:-1]           
    # Decouple "" into (+1)
    subset = [x.group() for x in regex.finditer(r'"(\w+ )*(\w+ ?)?"', query)]
    post = [regex.sub(r'(?<=\w+) +(?=\w+)', ' +1 ', x) for x in subset]
    for i in range(len(subset)):
        query = regex.sub(subset[i], "("+post[i][1:-1]+")", query, count=1)
    query = regex.sub(r'([()])', r" \1 ", query)

    query = regex.sub(r'(?<=(\n| |^)[^+/&( ]\w*) +(?=(\( *)* *\w+)', ' | ', query)
    query = query.split()

    print(parser.parse(query))

