import sys
import json
import regex
from sys import stdin

path_index = sys.argv[1]
index = None
with open(path_index) as f:
    index = f.read()
    index = json.loads(index)

print(index['shower'])

for line in stdin:
    query = line[:-1]
    query = regex.sub(r'([()])', r" \1 ", query)
    query = query.split()
    print(query)
