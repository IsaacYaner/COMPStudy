import sys
import json
import regex
from sys import stdin
from myparser import SimpleBooleanParser
# Write each operator below
# () > | > +n > /n > +s > /s > &
terms = {
'expression':       [r'\+', '-'],
'in_sentence':      [r'\*', '/'],
'factor':           [],
'word':             [],
}
parser = SimpleBooleanParser(terms)
query = input().split()
print(parser.parse(query))

