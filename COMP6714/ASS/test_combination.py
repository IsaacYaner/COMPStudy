from body import handle_query
import random
import json

def test_and_or_rand():
    # vocabulary = ['plugin', 'company',  'revenue', 's', 'monster']
    with open('vocabularies') as f:
        vocabulary = json.load(f)
    for _ in range(1000):
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
