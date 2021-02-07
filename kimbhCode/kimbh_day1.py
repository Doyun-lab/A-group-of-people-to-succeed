
# coding: utf-8

# In[1]:


# 문제 1156
a = int(input())
if a % 2 == 0:
    print('even')
else:
    print('odd')


# In[3]:


# 문제 4531
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f = [a,b,c,d,e]
g = sorted(f)

print(int((a+b+c+d+e)/5))
print(g[2])


# In[4]:


# 문제 4501
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())

h = [a,b,c,d,e,f,g]

i = sorted(h)

print(i[6])
print(i[5])

