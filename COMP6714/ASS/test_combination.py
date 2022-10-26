from operator import or_
from body import handle_query
import random
import json
test_range = 1000

def test_and_or_rand():
    with open('vocabularies') as f:
        vocabulary = json.load(f)
    for _ in range(test_range):
        v1 = random.randrange(len(vocabulary))
        v2 = random.randrange(len(vocabulary))
        v3 = random.randrange(len(vocabulary))
        v4 = random.randrange(len(vocabulary))
        v1 = vocabulary[v1]
        v2 = vocabulary[v2]
        v3 = vocabulary[v3]
        v4 = vocabulary[v4]
        query = f'({v1} & {v2}) ({v3} & {v4})'
        factor = f'({v1} ({v3} & {v4})) & ({v2} ({v3} & {v4}))'
        factor = f'({v3} ({v1} & {v2})) & ({v4} ({v1} & {v2}))'
        assert(handle_query(query) == handle_query(factor))
    assert 3 == 3

def test_or_only():
    with open('vocabularies') as f:
        vocabulary = json.load(f)
    for _ in range(test_range):
        v1 = random.randrange(len(vocabulary))
        v2 = random.randrange(len(vocabulary))
        v1 = vocabulary[v1]
        v2 = vocabulary[v2]
        ans1 = handle_query(v1)
        ans2 = handle_query(v2)
        true_or = set(ans1)
        for i in ans2:
            true_or.add(i)
        or_query = f'{v1} {v2}'
        ans_or = set(handle_query(or_query))
        assert(true_or == ans_or)
    assert 3 == 3
    
def test_and_only():
    with open('vocabularies') as f:
        vocabulary = json.load(f)
    for _ in range(test_range):
        v1 = random.randrange(len(vocabulary))
        v2 = random.randrange(len(vocabulary))
        v1 = vocabulary[v1]
        v2 = vocabulary[v2]
        ans1 = handle_query(v1)
        ans2 = handle_query(v2)
        true_and = set()
        for i in ans2:
            if i in ans1:
                true_and.add(i)
        and_query = f'{v1} & {v2}'
        ans_and = set(handle_query(and_query))
        assert(true_and == ans_and)
    assert 3 == 3