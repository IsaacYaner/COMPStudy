import sys
import json
import regex
from sys import stdin
from myparser import SimpleBooleanParser

def is_operator(token):
    if token in '+-*/':
        return True
    return False

def get_value(token):
    return token

parser = SimpleBooleanParser()
for line in stdin:
    # Get rid of end of line
    query = line[:-1]           
    # Decouple "" into (+1)
    subset = [x.group() for x in regex.finditer(r'"(\w+ )*(\w+ ?)?"', query)]
    post = [regex.sub(r'(?<=\w+) +(?=\w+)', ' +1 ', x) for x in subset]
    for i in range(len(subset)):
        query = regex.sub(subset[i], "("+post[i][1:-1]+")", query, count=1)
    query = regex.sub(r'([()])', r" \1 ", query)
    # print(query)
    query = regex.sub(r'(?<=(\n| |^)[^+/&( ]\w*) +(?=(\( *)* *\w+)', ' | ', query)
    query = query.split()
    # print(query)
    print(parser.parse(query))

