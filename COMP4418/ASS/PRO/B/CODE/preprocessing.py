import json
import pprint
from prefunctions import *
from windoz.windoz import Stopwatch
word = 'learning'

ith = 0
rounds = 0
result_list = []
timer = Stopwatch()
files = ['dblp-ref-0.json','dblp-ref-1.json','dblp-ref-2.json','dblp-ref-3.json']
with open('preprocessed.txt', 'w') as output:
    for f in files:
        with open(f) as file:
            while True:
                ith += 1
                data = file.readline()
                if data == '':
                    break
                result = preprocess(data, True)
                output.write(result)
                output.write('\n')
                if ith > 100000:
                    ith = 0
                    rounds += 1
                    print(rounds)
                # if word in data:
                    # obj = json.loads(data)
                    # result = {}
                    # # print(obj.keys())  
                    # result['id'] = obj['id']
                    # try:
                    #     result['ref'] = obj['references']
                    # except:
                    #     result['ref'] = []
                    # result_list.append(result)

# print(timer.read_and_set())
# pprint.pprint(len(result_list))