import json
import pprint
from prefunctions import *
from windoz.windoz import Stopwatch
word = 'learning'

ith = 0
rounds = 0
result_list = []
timer = Stopwatch()
files = ['rule.txt']
for f in files:
    with open(f) as file:
        with open('pre'+f, 'w') as output:
            while True:
                ith += 1
                data = file.readline()
                if data == '':  
                    break
                result = preprocess(data, link=True, to_lemmatize=True, remove_stop=False)
                output.write(str(result))
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