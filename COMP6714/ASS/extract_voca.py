import json
path_index = './index/index'
index = None
with open(path_index) as f:
    index = f.read()
    index = json.loads(index)
voca = list({token for token in index})
with open('vocabularies', 'w') as f:
    json.dump(voca, f)
print(len(voca))