# -*- coding: utf-8 -*-

# -- Sheet --

#Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
#sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd
df = pd.read_csv("california_housing_train.csv")
df.head(10)

df.info()

#Определить среднюю стоимость дома (median_house_value), где кол-во людей от 0 до 500 (population)

df.loc[(df['population'] <= 500) & (df['population'] > 0), 'median_house_value'].median()

#Задача 42: Узнать какая максимальная households в зоне минимального значения population
df[df['population'] == df['population'].min()]['households'].max()

