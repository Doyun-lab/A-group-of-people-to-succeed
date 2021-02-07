
# coding: utf-8

# In[1]:


# 문제 1170
a = input().split()

if int(a[2]) < 10:
    print(a[0]+a[1]+'0'+a[2])
else:
    print(a[0]+a[1]+a[2])


# In[4]:


# 문제 1267
a = int(input())
b = input().split()

c = []
for i, num in enumerate(b):
    if int(num) % 5 == 0:
        c.append(int(num))

d = 0
for i in c:
    d += i

print(d)


# In[13]:


# 문제 1093
a = int(input())
b = input().split()

c = []
for i in range(23):
    c.append(0)

for i, num in enumerate(b):
    c[int(num)-1] += 1

for i in c:
    print(i, end=' ')

