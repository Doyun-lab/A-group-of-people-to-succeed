
# coding: utf-8

# In[1]:


# 문제 1074
a = int(input()) + 1

while a > 0:
    a -= 1
    print(a)
    if a==1:
        break


# In[ ]:


# 문제 1721
import math
a = input().split()
b = input().split()

print('%0.2f' % math.sqrt((int(a[0]) - int(b[0]))**2 + (int(a[1]) - int(b[1]))**2))


# In[23]:


# 문제 2779
i = 0
while i < 10:
    i += 1
    globals()['area_{}'.format(i)] = input().split()
    print(globals()['area_{}'.format(i)])
    
area = []
for i in range(10):
    area.append(globals()['area_{}'.format(i+1)])
    
for i in range(10):
    globals()['index{}'.format(i+1)] = [int(i) for i, value in enumerate(area[i]) if value == '1']


# In[33]:


indexs = []
for i in range(10):
    indexs.append(globals()['area_{}'.format(i+1)])


# In[47]:


by2 = 0
by3 = 0
by4 = 0

n = 9
while n >= 6:
    if n==9:
        k = n
    for i in range(k):
        for j in range(k):
            if k==9:
                if indexs[i][j]=='1' and indexs[i][j+1]=='1' and indexs[i+1][j]=='1' and indexs[i+1][j+1]=='1':
                    globals()['by{}'.format(i+2)] += 1
            elif k==8:
                if indexs[i][j]=='1' and indexs[i][j+1]=='1' and indexs[i][j+2]=='1' and indexs[i+1][j]=='1' and indexs[i+1][j+1]=='1' and indexs[i+2][j]=='1':
                    globals()['by{}'.format(i+2)] += 1
    k = n-1


# In[ ]:


by2


# In[43]:


globals()['by{}'.format(i+2)] += 1


# In[46]:


n

