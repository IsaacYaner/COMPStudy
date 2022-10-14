import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
stopwords = stopwords.words('english')

'''
input:  list
output: list
'''
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

def preprocess(text, link=False, to_lemmatize=False, fix_quotation=True):
    text = word_tokenize(text)
    text = remove_stop_words(text)
    text = normalise(text)
    if to_lemmatize:
        text = lemmatize(text)
    else:
        text = stem(text)
    if fix_quotation:
        text = [re.sub(r'``', r'"', tk) for tk in text]
        text = [re.sub(r'\'\'', r'"', tk) for tk in text]
    if link:
        return " ".join(text)
    return text
text = "Hello, my name is laoyanging, reliable, reliability, dogs!"
text = preprocess(text)
print(text)