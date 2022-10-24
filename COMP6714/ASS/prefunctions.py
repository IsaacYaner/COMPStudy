import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
import regex
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
        text = [re.sub(r'``', r'"', tk) for tk in text]
        text = [re.sub(r'\'\'', r'"', tk) for tk in text]
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


# text = "Hello, my name is laoyanging, reliable, reliability, dogs!"
# text = preprocess(text)
# print(text)