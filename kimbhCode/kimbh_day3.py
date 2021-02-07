
# coding: utf-8

# In[18]:


# 문제 1081
a = input().split()

for i in range(int(a[0])):
    for j in range(int(a[1])):
        print(str(i+1) +' ' + str(j+1))


# In[20]:


# 문제 1228
a = input().split()

b = (float(a[0])-100) * 0.9
c = float((float(a[1])-b) * 100 / 63)

if c <= 10:
    print('정상')
elif c > 10 and c <=20:
    print('과체중')
else:
    print('비만')


# In[42]:


# 문제1096
a = int(input())
for i in range(a):
    globals()['b_{}'.format(i)] = input().split()

c = []
d = []
for i in range(19):
    for j in range(19):
        d.append(0)
    c.append(d)
    d = []

for i in range(a):
    e = int(globals()['b_{}'.format(i)][0])
    f = int(globals()['b_{}'.format(i)][1])
    c[e-1][f-1] = 1
    
for i in range(19):
    for j in range(19):
        print(c[i][j], end=' ')
    print()

