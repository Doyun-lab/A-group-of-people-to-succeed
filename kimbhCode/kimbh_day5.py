
# coding: utf-8

# In[24]:


# 문제 4651
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

d = [0, 0, 0]
for i in range(3):
    if i == 0:
        for j in a:
            if j == 1:
                d[i] += 1
    elif i == 1:
        for k in b:
            if k == 1:
                d[i] += 1
    else:
        for l in c:
            if l == 1:
                d[i] += 1
        
        for h in d:
            if h==0:
                print('D')
            elif h==1:
                print('C')
            elif h==2:
                print('B')
            elif h==3:
                print('A')
            else:
                print('E')


# In[25]:


# 문제 1734
a = input()
print('welcome! {}'.format(a))


# In[26]:


# 문제 4891
a = int(input())
b = [int(i) for i in input().split()]

print(max(b) - min(b))

