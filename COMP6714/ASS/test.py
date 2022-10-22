import sys
import json
import regex
from sys import stdin

def is_operator(token):
    if token in '+-*/':
        return True
    return False

def get_value(token):
    return token

for line in stdin:
    query = line[:-1]
    subset = [x.group() for x in regex.finditer(r'"(\w+ )*(\w+ ?)?"', query)]
    post = [regex.sub(r'(?<=\w+) +(?=\w+)', '+1', x) for x in subset]
    for i in range(len(subset)):
        query = regex.sub(subset[0], "("+post[0][1:-1]+")", query, count=1)
    print(subset)
    print(query)


