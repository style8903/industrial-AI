#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = int(input("정수 x="))


# In[2]:


x


# In[3]:


if(x%2 == 1) :
    print("홀수입니다.")
else :
    print("짝수입니다.")


# In[4]:


score = int(input("정수"))


# In[5]:


if(score >= 90):
    print("A학점")
elif (score >= 80) :
    print("B학점")
elif (score >= 70) :
    print("C학점")
elif (score >= 60) :
    print("D학점")
else :
    print("F학점")


# In[6]:


sum = 0
for i in range(1,10):
    sum += i


# In[7]:


sum


# In[8]:


oddsum = 0
for i in range(1,101, 2):
    oddsum += i


# In[9]:


oddsum


# In[10]:


evensum = 0
for i in range(2, 100, 2):
    evensum += i


# In[11]:


evensum


# In[12]:


sum = 0


# In[13]:


score = [12, 24, 56, 25, 67]
for data in score:
    sum += data    


# In[14]:


sum


# In[15]:


def su(a,b):
    c = a+b
    return c


# In[16]:


m = su(4,7)


# In[17]:


m


# In[ ]:




