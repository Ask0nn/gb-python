from sklearn.preprocessing import LabelBinarizer
import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
_data = LabelBinarizer().fit_transform(data.whoAmI)

