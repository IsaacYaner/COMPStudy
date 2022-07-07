from contextlib import suppress
import re
import itertools
from unittest import result
def read_data():
    with open('q1.txt', 'r') as f:
        data = f.read()
        data = data.split('\n')
        for i in range(len(data)):
            data[i] = data[i].split(' ')
        data = [i[:-1] for i in data]
        return data

def in_trans(item, transaction):
    for i in item:
        if not i in transaction:
            return False
    return True

def get_support(item, transactions):
    result = 0
    for t in transactions:
        if in_trans(item, t):
            result += 1
    return result

def get_set(data):
    result = set()
    for i in data:
        for j in i:
            result.add((j,))
    return result

def get_count():
    support = {}
    with open('q1.txt', 'r') as f:
        data = f.read()
        data = data.replace('\n', ' ')
        data = data.replace('  ', ' ')
        data = data.split(' ')
        for i in data:
            try:
                support[i] += 1
            except:
                support[i] = 1
    del support['']
    result = {}
    for i in support:
        if support[i] >= 100:
            result[i] = support[i]
    return result

def get_filtered():
    result = get_count()
    return [r for r in result]
 
threshold = 100
max_set = 2
C = []
L = []
L.append(get_count())
C.append(get_set(L))
# print(C)
def lin(data):
    sum = 0
    for i in data:
        sum += len(i)
    return sum
def simple_data():
    result = []
    fil = get_filtered() 
    data = read_data()
    for i in data:
        row = []
        for j in i:
            if j in fil:
                row.append(j)
        if row != []:
            result.append(row)
    return result
data = simple_data()
print(lin(data))
# for i in range(1, max_set):
#     freq = {}
#     for item in C[i]:
#         count = get_support(item, data)
#         freq[item] = count
#     L.append(freq)
# iterable = C[0]
# print(len(C[0]))
# data = itertools.combinations(iterable, 2)
# for d in data:
#     print(d)
# print(L)
