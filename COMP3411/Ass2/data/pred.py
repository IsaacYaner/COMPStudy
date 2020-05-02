import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import tree
data = pd.read_csv("W:/UNSWSTUDY/COMPStudy/COMP3411/Ass2/data/adult.data", sep=',')
y = data.slr 
X = data.drop('slr', axis = 1)
scaledX = preprocessing.scale(X)
