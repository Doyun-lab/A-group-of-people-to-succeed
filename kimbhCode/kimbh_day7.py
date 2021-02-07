
# coding: utf-8

# In[31]:


# 문제 1230
a = [int(x) for x in input().split()]

b = []
c = []
for idx, num in enumerate(a):
    if a[idx] <= 170:
        b.append(idx)
    else:
        c.append(idx)
        
if len(b) >= 1:
    print('CRASH ' + str(a[b[0]]))
else:
    print('PASS')


# In[39]:


# 문제 1085
a= [int(x) for x in input().split()]

bit = a[0] * a[1] * a[2] * a[3]
byte = bit/8
KB = byte/1024
MB = KB/1024
MB_r = round(MB, 1)

print(str(MB_r) + ' MB')


# In[90]:


# 문제 1026(백준)
S = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

c = 0
for i in range(S):
    c += A.pop(A.index(max(A))) * B.pop(B.index(min(B)))
print(c)

