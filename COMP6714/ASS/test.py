from prefunctions import sb_pre

# tokenizer = RegexpTokenizer(r'\w+', gaps=True)
# data = tokenizer.tokenize('EEighty-seven miles to go, yet.  Onward!')
# print(" ".join(data))
my_string = 'Cat\'s shoe\'s cats\' tom\'s hoBys\'.\n\
I\'m Can\'t Let\'s It\'s He\'s She\'s there\'s here\'s\n\
Hello, I\'m a U.S. doctor Mr. Marie.\n\
Mrs. Mr. C.N.N. U.S.A. U.K. etc. ETC. Etc. e.g. a.m. p.m. i.e. e.g. p.p. \n\
I love pineapple. I love it! Do you know Corns?\
Door-dash'


data = sb_pre(my_string, link=True)
print(data)