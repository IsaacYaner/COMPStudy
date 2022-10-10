import json
import pprint
word = 'learning'

result_list = []
with open('dblp-ref-0.json') as file:
    for i in range(1000):
        data = file.readline()
        if word in data:
            obj = json.loads(data)
            result = {}
            print(obj.keys())
            result['id'] = obj['id']
            try:
                result['ref'] = obj['references']
            except:
                result['ref'] = []
            result_list.append(result)

pprint.pprint(result_list)