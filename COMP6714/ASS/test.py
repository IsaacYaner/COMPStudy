from prefunctions import sb_pre

# tokenizer = RegexpTokenizer(r'\w+', gaps=True)
# data = tokenizer.tokenize('EEighty-seven miles to go, yet.  Onward!')
# print(" ".join(data))
my_string =  "A study group said the United States\
  should increase its strategic petroleum reserve to one mln\
  barrels as one way to deal with the present and future impact\
  of low oil prices on the domestic oil industry.\
      U.S. policy now is to raise the strategic reserve to 750\
  mln barrels, from its present 500 mln, to help protect the\
  economy from an overseas embargo or a sharp price rise.\
      The Aspen Institute for Humanistic Studies, a private\
  group, also called for new research for oil exploration and\
  development techniques.\
      It predicted prices would remain at about 15-18 dlrs a\
  barrel for several years and then rise to the mid 20s, with\
  imports at about 30 pct of U.S. consumption.\
      It said instead that such moves as increasing oil reserves\
  and more exploration and development research would help to\
  guard against or mitigate the risks of increased imports."

data = sb_pre(my_string, link=False)
print(data)