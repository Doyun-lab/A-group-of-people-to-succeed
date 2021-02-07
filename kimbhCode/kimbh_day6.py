
# coding: utf-8

# In[4]:


# 문제 1920
a = int(input())
# for라는 문자열을 인식해서 안됨
# print(format(a,'b'))
print(bin(a)[2:])


# In[10]:


# 문제 1451
a = int(input())
b=[]
for i in range(a):
    b.append(int(input()))

b.sort()
for i in b:
    print(i)


# In[21]:


# 문제 2055 (시간초과)
a = [int(x) for x in input().split()]

for i in range(1,a[1]+1):
    if a[0] % i == 0 or a[1] % i == 0:
        print(i, end=' ')


# In[49]:


# 문제 2055
import math
a = [int(x) for x in input().split()]

b = []
for i in range(1,int(math.sqrt(a[0]))+1):
    if a[0] % i == 0:
        b.append(i)
        b.append(a[0]//i)

for i in range(1,int(math.sqrt(a[1]))+1):
    if a[1] % i == 0:
        b.append(i)
        b.append(a[1]//i)

c = list(set(b))
c.sort()        

for i in c:
    print(i, end=' ')

