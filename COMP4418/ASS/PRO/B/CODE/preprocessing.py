import json
import pprint
from windoz.windoz import Stopwatch
word = 'learning'


result_list = []
timer = Stopwatch()

with open('dblp-ref-0.json') as file:
    while True:
        data = file.readline()
        if data == '':
            break
        if word in data:
            obj = json.loads(data)
            result = {}
            # print(obj.keys())
            result['id'] = obj['id']
            try:
                result['ref'] = obj['references']
            except:
                result['ref'] = []
            result_list.append(result)

print(timer.read_and_set())
pprint.pprint(len(result_list))