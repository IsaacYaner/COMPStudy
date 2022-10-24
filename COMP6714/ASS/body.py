from cgitb import handler
from lib2to3.pgen2.literals import simple_escapes
from operator import or_
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

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def all_docs(index):
    result = []

import copy
# Or queries takes all information together
# token: takes all
# doc: takes all
# location: takes all
def or_query(dest, src, op):
    result = copy.deepcopy(dest)
    for token in src:
        if token in dest:
            for doc in src[token]:
                if doc in dest[token]:
                    temp_list = []
                    i,j = 0,0
                    while True:
                        if i == len(dest[token][doc]):              # i reaches end of dest
                            if src[token][doc][j] not in temp_list: # append src[j]
                                temp_list.append(src[token][doc][j])# append src[j]
                            j += 1
                        elif j == len(src[token][doc]):                 # j reaches end of src
                            if dest[token][doc][i] not in temp_list:  # append result[i]
                                temp_list.append(dest[token][doc][i]) # append result[i]
                            i += 1
                        elif dest[token][doc][i] > src[token][doc][j]:# result[i] larger than src[j]
                            if src[token][doc][j] not in temp_list:     # append smaller src[j]
                                temp_list.append(src[token][doc][j])    # append smaller src[j]
                            j += 1
                        else:
                            if dest[token][doc][i] not in temp_list:  # result[i] smaller
                                temp_list.append(dest[token][doc][i]) # append result[i]
                            i += 1
                        if i==len(dest[token][doc]) and j==len(src[token][doc]):
                            break
                    result[token][doc] = temp_list
                else:
                    result[token][doc] = src[token][doc]
        else:
            result[token] = src[token]
    return result

def all_docs(index):
    return list({doc for token in index for doc in index[token] })
def intersection(dest, src):
    temp_list = []
    i,j = 0,0
    while True:
        if i == len(dest) or j == len(src):
            break
        if dest[i] > src[j]:
            j += 1
        elif dest[i] < src[j]:
            i += 1
        else:
            temp_list.append(dest[i])
            i += 1 
            j += 1
    return temp_list
def intersection_doc(lst1, lst2):
    return [value for value in lst1 if value in lst2]
def filter_docs(doc_list, selected_docs):
    result = {}
    for doc in doc_list:
        if doc in selected_docs:
            result[doc] = doc_list[doc]
    return result
def and_query(dest, src, op):
    selected_docs = intersection_doc(all_docs(dest), all_docs(src))
    # print(all_docs(dest), all_docs(src))
    # print(selected_docs)
    result = {}
    for token in src:
        if token not in dest:
            temp_doc = filter_docs(src[token], selected_docs)
            if temp_doc != {}:
                result[token] = temp_doc
        else:
            result[token] = {}
            for doc in src[token]:
                if doc in dest[token]:
                    left = dest[token][doc]
                    right = src[token][doc]
                    common_position = intersection(left, right)
                    if common_position != []:
                        result[token][doc] = common_position
            if result[token] == {}:
                del result[token]
    for token in dest:
        if token not in src:
            temp_doc = filter_docs(dest[token], selected_docs)
            if temp_doc != {}:
                result[token] = temp_doc
    return result

# TODO change back later
# path_index = sys.argv[1]
path_index = './index/index'
index = None
with open(path_index) as f:
    index = f.read()
    index = json.loads(index)

# print(index['shower'])

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
'expression':       and_query,
'in_sentence':      echo_expression,
'after_sentence':   echo_expression,
'in_n':             echo_expression,
'after_n':          echo_expression,
'term':             or_query,
} 
def value(text):
    try: 
        text = normalise([text])
        text = stem(text)
        return {text[0] : index[text[0]]}
    except:
        return {}
parser = SimpleBooleanParser(terms, operations, value)

def handle_query(query):   
    # Decouple "" into (+1)
    subset = [x.group() for x in regex.finditer(r'"(\w+ )*(\w+ ?)?"', query)]
    post = [regex.sub(r'(?<=\w+) +(?=\w+)', ' +1 ', x) for x in subset]
    for i in range(len(subset)):
        query = regex.sub(subset[i], "("+post[i][1:-1]+")", query, count=1)
    query = regex.sub(r'([()])', r" \1 ", query)

    query = regex.sub(r'(?<=(\n| |^)[^+/&( ]\w*) +(?=(\( *)* *\w+)', ' | ', query)
    query = query.split()
    # print(query)
    answer = parser.parse(query)
    result = set()
    for a in answer:
        for doc in answer[a]:
            result.add(int(doc))
    result = sorted(result)
    return result


if __name__ == '__main__':
    for line in stdin:
        # Get rid of end of line
        query = line[:-1]    
        result = handle_query(query)
        for r in result:
            print(r)
        # print(len(result))

