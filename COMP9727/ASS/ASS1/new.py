from contextlib import suppress
import re

def read_data():
    support = {}
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
    return support
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
data = get_count()
print(len(data))