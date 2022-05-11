import pandas as pd
import numpy as np

#1
s = pd.Series(5, index=[0,1,2,3])
print(s)
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

#2
data = {'a':0. , 'b':1. , 'c':2.}
s = pd.Series(data)
print(s)
s = pd.Series(data, index=['b','c','d','a'])
print(s)

#3
s = pd.Series(np.random.randn(4))
print(s)
print(s.axes)
print(s.ndim)
print(s.size)

#4
s = pd.Series([1,2,3,4,5], index= list('abcde'))
print(s[0])
print(s[:3])
print(s['a'])
print(s[['a', 'c', 'd']])

#5
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([4,5,6], index=['c','a','b'])
s3 = s1 + s2
print(s1)
print(s2)
print(s3)

#6
data = ['A', 'B', 'C']
df = pd.DataFrame(data)
print(df)
print(df.T)
data = [['A', 'B', 'C'], ['D', 'E', 'F']]
df = pd.DataFrame(data)
print(df)
print(df.T)

#7
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, colums= ['Name', 'Age'])
print(df)
data = {'Name':['A','B','C','D'], 'Age': [28,34,29,42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
data = [{'a': 1, 'b': 2}, {'a':5, 'b':10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a','b'])
print(df1)
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a','b1'])
print(df2)
df3 = pd.DataFrame(data, index=['first', 'second'], columns=['a','c'])
print(df3)

#8
dates = pd.date_range('20200901', periods=6)
df = pd.DataFrame(np.random.randn(6,2), index=dates, columns=list('AB'))
print(df)
print(df.index)
print(df.columns)
print(df.values)

df = pd.DataFrame({ 'B': pd.Timestamp('20200927'),
                    'A': '삼성',
                    'C': pd.Series([1000.5, 900.0, 950.0, 1100.0], index=list(range(4)), dtype='float32'),
                    'D': np.array([10, 30, 40, 20], dtype='int32'),
                    'E': pd.Categorical(['kindA', 'kindB', 'kindC', 'kindC']),
                    'F': 'smart phone'})
print(df)

#9
df = pd.DataFrame([[1,2], [3,4]], columns=['a','b'])
df2 = pd.DataFrame([[5,6], [7,8]], columns=['a','b'])
df = df.append(df2)
print(df)
df = df.drop(0)
print(df)

#10
s = pd.Series(np.random.randn(50))
print(s.sample(n = 3))
df = pd.DataFrame(np.random.randn(50,4), columns=list('ABCD'))
print(df.sample(frac=0.1, replace=True))

#11
df = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['a','b'])
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.mean(1))