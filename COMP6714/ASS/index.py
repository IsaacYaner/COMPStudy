import os
import sys

path_documents = sys.argv[1]
path_index = sys.argv[2]

documents = os.listdir(path_documents)

print(len('Total number of documents:'))
for filename in documents:
#    with open(os.path.join(os.getcwd(), filename), 'r') as f:
