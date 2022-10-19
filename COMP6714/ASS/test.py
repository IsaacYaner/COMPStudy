from re import IGNORECASE
import regex
from nltk.tokenize import RegexpTokenizer

def clean_text(rgx_list, text, flags=[regex.IGNORECASE for dom in range(10)]):
    new_text = text
    i = 0
    for rgx_match in rgx_list:
        new_text = regex.sub(rgx_match, '', new_text, flags=flags[i])
        i += 1
    return new_text
# tokenizer = RegexpTokenizer(r'\w+', gaps=True)
# data = tokenizer.tokenize('EEighty-seven miles to go, yet.  Onward!')
# print(" ".join(data))
my_string = 'Cat\'s shoe\'s cats\' tom\'s hoBys\'.\n\
I\'m Can\'t Let\'s It\'s He\'s She\'s there\'s here\'s\n\
Hello, I\'m a U.S. doctor Mr. Marie.\n'
ignore_list = [r"(?<!(can|let|it|he|she|there|here|that|this))'(?=[s .])", "(?<=[A-Z])\.(?=[A-Z ,.\n])"]
flags = [regex.IGNORECASE, 0]
# data = regex.findall(PATTERN, my_string)
data = clean_text(ignore_list, my_string, flags)
print(data)