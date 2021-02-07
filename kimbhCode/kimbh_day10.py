
# coding: utf-8

# In[ ]:


# 문제 3047

# 이 문제는 접근법을 모르겠음 (알고리즘 공부 후 풀기)


# In[10]:


# 문제 4877
import numpy as np

a = [int(x) for x in input().split()]

n = a[3]
del a[3]

b = []
for i in range(0, 50):
    for j in range(0,50):
        for h in range(0,50):
            b.append(sum(np.array(a) * np.array([i,j,h])))

if n in b:
    print(1)
else:
    print(0)


# In[19]:


# 문제 1615
aa = [int(x) for x in input().split()]

def d(x):
    a = list(str(x))
    b = 0
    for i in a:
        b += int(i)
    b += x
    return b

p = []
for i in range(1, 5001):
    p.append(d(i))

nn = 0
for i in range(aa[0], aa[1]+1):
    if i not in p:
        nn += i
        
print(nn)


# In[20]:


nn


# In[15]:


aa


# In[18]:




