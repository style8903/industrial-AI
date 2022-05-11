import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#1
plt.style.use('fivethirtyeight')
warnings.filterwarnings('ignore')

data = pd.read_excel('titanic.xlsx')
data.head()

for col in data.columns:
    msg = 'column: {:>10}\t Percent of NaN value: {:.2f}%'.format(col,
                                                                  100 * (data[col].isnull().sum() / data[col].shape[0]))
    print(msg)

f, ax = plt.subplots(1, 2, figsize=(18, 8))

data['survived'].value_counts().plot.pie(explode= [0,0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Pie plot - survived')
ax[0].set_ylabel('')
sns.countplot('survived', data=data, ax=ax[1])
ax[1].set_title('Count plot - survived')

plt.show()

#2
data[['pclass', 'survived']].groupby(['pclass'], as_index=True).count()
pd.crosstab(data['pclass'], data['survived'], margins=True).style.background_gradient(cmap='summer_r')
data[['pclass', 'survived']].groupby(['pclass'], as_index=True).mean().sort_value(by='survived', ascending=False).plot.bar()

#3
fig, ax = plt.subplots(1,1, figsize=(9, 5))
sns.kdeplot(data[data['survived'] == 1]['age'], ax=ax)
sns.kdeplot(data[data['survived'] == 0]['age'], ax=ax)
plt.legend(['survived == 1', 'survived == 0'])
plt.show()

plt.figure(figsize=(8,6))
data['age'][data['pclass'] == 1].plot(kind='kde')
data['age'][data['pclass'] == 2].plot(kind='kde')
data['age'][data['pclass'] == 3].plot(kind='kde')

plt.xlabel('나이')
plt.title('pclass내에 나이 분포')
plt.legend(['1st Class', '2nd Class', '3rd Class'])

cummulate_survival_ratio = []
for i  in range(1, 80):
    cummulate_survival_ratio.append(data[data['age'] < i]['survived'].sum()
                                    / len(data[data['age'] < i]['survived']))

plt.figure(figsize=(7,7))
plt.plot(cummulate_survival_ratio)
plt.title('나이에 따른 생존 비율', y= 1.02)
plt.ylabel('생존비율')
plt.xlabel('나이의 범위(0~x)')
plt.show()

#4
f, ax= plt.subplots(1,2,figsize=(18,8))
sns.violinplot('pclass', 'age', hue='survived', data= data, scale='count', split=True, ax=ax[0])
ax[0].set_title('pclass and age vs survived')
ax[0].set_yticks(range(0, 110, 10))
sns.violinplot('sex', 'age', hue='survived', data= data, scale='count', split=True, ax=ax[1])
ax[1].set_title('sex and age vs survived')
ax[1].set_yticks(range(0, 110, 10))
