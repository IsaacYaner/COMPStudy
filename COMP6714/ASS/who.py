a = {'A':{'doc1':[], 'doc2':[1], 'doc3':[2]},'B':{'doc1':[], 'doc3':[]}}
b = {'A':{'doc2':[1], 'doc3':[2]},'C':{'doc3':[1]}}
def all_docs(index):
    return list({doc for token in index for doc in index[token] })
def intersection_doc(lst1, lst2):
    return = [value for value in lst1 if value in lst2]
def intersection(dest, src):
    temp_list = []
    i,j = 0,0
    while True:
        if i == len(dest) or j == len(src):
            break
        if dest[i] > src[j]:
            j += 1
        elif dest[i] < src[j]:
            i += 1
        else:
            temp_list.append(dest[i])
            i += 1 
            j += 1
    return temp_list
def filter_docs(doc_list, selected_docs):
    result = {}
    for doc in doc_list:
        if doc in selected_docs:
            result[doc] = doc_list[doc]
    return result
# selected_docs = intersection(all_docs(a), all_docs(b))
# data = all_docs(b)
# data = filter_docs(b['C'], [])
# print(data)
def and_query(dest, src, op):
    selected_docs = intersection(all_docs(dest), all_docs(src))
    result = {}
    for token in src:
        if token not in dest:
            temp_doc = filter_docs(src[token], selected_docs)
            if temp_doc != {}:
                result[token] = temp_doc
        else:
            result[token] = {}
            for doc in src[token]:
                if doc in selected_docs:
                    left = dest[token][doc]
                    right = src[token][doc]
                    common_position = intersection(left, right)
                    if common_position != []:
                        result[token][doc] = common_position
            if result[token] == {}:
                del result[token]
    for token in dest:
        if token not in src:
            temp_doc = filter_docs(dest[token], selected_docs)
            if temp_doc != {}:
                result[token] = temp_doc
    return result
data = and_query(a, b, 1)
print(data)