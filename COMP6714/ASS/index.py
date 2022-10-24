import os
import sys
import json
import nltk
import regex
from nltk.corpus import stopwords
from nltk import word_tokenize

stopwords = stopwords.words('english')
def remove_stop_words(tokens):
    return [w for w in tokens if w not in stopwords]

def normalise(tokens):
    tokens = [tk.lower() for tk in tokens]
    return tokens

def stem(tokens):
    porter = nltk.PorterStemmer()
    return [porter.stem(tk) for tk in tokens]

def lemmatize(tokens):
    wnl = nltk.WordNetLemmatizer()
    return [wnl.lemmatize(tk) for tk in tokens]

def preprocess(text, link=False, to_lemmatize=False, fix_quotation=True, remove_stop=True):
    text = word_tokenize(text)
    if remove_stop:
        text = remove_stop_words(text)
    text = normalise(text)
    if to_lemmatize:
        text = lemmatize(text)
    else:
        text = stem(text)
    if fix_quotation:
        text = [regex.sub(r'``', r'"', tk) for tk in text]
        text = [regex.sub(r'\'\'', r'"', tk) for tk in text]
    if link:
        return " ".join(text)
    return text

def clean_text(rgx_list, text, flags=[regex.IGNORECASE for dom in range(10)]):
    new_text = text
    i = 0
    for rgx_match in rgx_list:
        new_text = regex.sub(rgx_match, '', new_text, flags=flags[i])
        i += 1
    return new_text

def remove_punctuations(text):
    ignore_list = [r"(?<!(can|let|it|he|she|there|here|that|this))'(?=[s .])", r"(?<=\.[a-z])\.(?=[ ])", r"(?<=[a-z])\.(?=[a-z])", r"(?<=([A-Z][rs]*|[eE][tT][cC]))\.(?=[A-Z ,.\n])"]
    flags = [regex.IGNORECASE,regex.IGNORECASE,regex.IGNORECASE, 0]
    # data = regex.findall(PATTERN, my_string)
    return clean_text(ignore_list, text, flags)

def sb_pre(text, link=False):
    text = remove_punctuations(text)                # Remove unwanted punctuations
    text = regex.sub(r'[^\w!?. \n]', ' ',text)      # Clean all invalid characters
    text = regex.sub(r"(?<![A-Za-z]+[^A-Za-z \n]*)[0-9]*([^A-Za-z \n]+[0-9]+)?(?![^A-Za-z\n ]*[A-Za-z])\b", '', text)
                                                    # Remove pure numbers
    text = regex.sub(r'[!?.]', '.',text)            # Place sentence separator
    text = word_tokenize(text)
    text = normalise(text)
    text = stem(text)
    text = [t if regex.match("^[0-9]*$", t) is None else t+'s' for t in text]
    if link:
        return " ".join(text)
    return text


num_tokens = 0
def add_to_index(index, doc, tokens):
    global num_tokens
    for token, pos in zip(tokens, range(len(tokens))):
        num_tokens += 1
        if token in list(index.keys()):
            if doc in list(index[token].keys()):
                index[token][doc].append(pos)
            else:
                index[token][doc] = [pos]
        else:
            index[token] = {doc:[pos]}

path_documents = sys.argv[1]
path_index = sys.argv[2]

documents = os.listdir(path_documents)

index = {}
for filename in documents:
    with open(os.path.join(path_documents,filename), 'r') as fp:
        data = fp.read()
        data = sb_pre(data)#, True)
        add_to_index(index, filename, data)
with open(os.path.join(path_index, 'index'), 'w') as wrt: # TODO remove later
    wrt.write(json.dumps(index))
print('Total number of documents: ', len(documents))
print('Total number of tokens: ', num_tokens)
print('Total number of terms: ', len(list(index.keys())))
#    with open(os.path.join(os.getcwd(), filename), 'r') as f:
