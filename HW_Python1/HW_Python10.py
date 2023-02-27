
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

#используем get_dummies
pd.get_dummies(data['whoAmI'])

#используем OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()
data_new = onehotencoder.fit_transform(data.values)
pd.DataFrame(data_new.toarray(),
columns=onehotencoder.categories_)



