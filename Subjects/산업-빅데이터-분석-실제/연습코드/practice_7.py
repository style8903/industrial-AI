import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

#1
data = pd.read_excel('titanic.xlsx')
print(data.head())
print(data.info())
print(data.isnull().sum())

#2
print(data.columns)
data.rename(columns={'survived': 'SURVIVED'}, inplace=True)
print(data.columns)
data.drop(columns='class', inplace=True)
print(data)

#3
ddd = pd.Series(['Dog', 'Cat', 'Dog', 'Cat', 'Bat'])
ddd.duplicated()

#4
data.drop_duplicates(inplace=True)
data.isnull().head(10)
data.isnull().sum()
data.dropna(inplace=True)

#5
data['age'].fillna(data['age'].mean(), inplace=True)
data.isnull().sum()

#6
ddd = pd.Series([4,5,6,7,8,9])
ddd.replace(4, 10)

#7
dpd = pd.DataFrame({'X':[0,1,2,3,4,5],
                    'Y':[6,7,8,9,10,11],
                    'Z':['a','b','c','d','e','f']})
print(dpd)
print(dpd.replace(0,11))
dd1 = dpd.replace(0, 11)
print(dd1.replace(11,40))

#8
data.replace({'sex': {'male': 0}}, inplace= True)
data.replace({'sex': {'female': 1}}, inplace= True)

#9
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

le = LabelEncoder()
data['who_labeled'] = le.fit_transform(data.who)
data.describe()

scaler = MinMaxScaler()
data[['fare']] = scaler.fit_transform(data[['fare']])
data.describe()

data['fare'].plot(kind="box")
data.drop(data[data.fare >= 1].index, inplace= True)
data['fare'].plot(kind = "box")
