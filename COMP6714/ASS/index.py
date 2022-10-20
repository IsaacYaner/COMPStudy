import os
import sys
import json
import regex
from prefunctions import sb_pre
num_tokens = 0
def add_to_index(index, doc, tokens):
    global num_tokens
    for token, pos in zip(tokens, range(len(tokens))):
        num_tokens += 1
        if token in list(index.keys()):
            if doc in list(index[token].keys()):
                index[token][doc].append(pos)
            else:
                index[token][doc] = [pos]
        else:
            index[token] = {doc:[pos]}

path_documents = sys.argv[1]
path_index = sys.argv[2]

documents = os.listdir(path_documents)
                


index = {}
for filename in documents:
    with open(os.path.join(path_documents,filename), 'r') as fp:
        data = fp.read()
        data = sb_pre(data)#, True)
        add_to_index(index, filename, data)
with open(os.path.join(path_index, 'index'), 'w') as wrt: # TODO remove later
    wrt.write(json.dumps(index))
print('Total number of documents: ', len(documents))
print('Total number of tokens: ', num_tokens)
print('Total number of terms: ', len(list(index.keys())))
#    with open(os.path.join(os.getcwd(), filename), 'r') as f:
