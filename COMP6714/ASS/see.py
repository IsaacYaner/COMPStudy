from index import *

path_documents = 'nf'
filename = '1272'
index = {}
with open(os.path.join(path_documents,filename), 'r') as fp:
    data = fp.read()
    data = sb_pre(data)#, True)
    print(data)


# path_index = './index/dots'
# import json
# with open(path_index) as f:
#     data = json.load(f)

# documents = os.listdir(path_documents)
# for fn in documents:
#     if fn not in data:
#         print(fn)