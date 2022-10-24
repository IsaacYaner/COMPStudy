import os
import regex
path_documents = 'nf'

documents = os.listdir(path_documents)

index = {}

def inspect(text):
    result = []
    for filename in documents:
        with open(os.path.join(path_documents,filename), 'r') as fp:
            data = fp.read()
            data = regex.findall(text, data)
            if data != []:
                data = [filename+':\t'+x for x in data]
                result.append(data)
    return result

data = inspect(r'...nj...')
data = [x for sublist in data for x in sublist]
data = '\n'.join(map(str, data))
print(data)