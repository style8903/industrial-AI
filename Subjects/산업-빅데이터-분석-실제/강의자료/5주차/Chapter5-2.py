#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import time


# In[3]:


n = 1000
m = 5000

# X 행렬 : 크기 1000 X 5000
# W 행렬 : 크기 1000 X 1
# Z = W*X


# In[4]:


X = np.random.rand(n,m)
W = np.random.rand(n,1)
Z = np.zeros((1, m))


# In[5]:


start_time  = time.time()
for i in range (X.shape[1]) :
    for j in range(X.shape[0]):
        Z[0][i] += W[j]*X[j][i]
end_time = time.time()
print("반복문 이용 실행시간: ", (end_time - start_time)*1000, "ms")


# In[6]:


start_time = time.time()
Z = np.dot(W.T, X)
end_time = time.time()
print("numpy 이용 실행시간 : ", (end_time - start_time)*1000, "ms")


# In[8]:


x = np.float32(1.0)


# In[9]:


x


# In[ ]:




