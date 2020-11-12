# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:52:38 2020

@author: a0105
"""

# 1230
a, b, c = map(int, input().split())

if a <= 170:
    print("CRASH",a)
    
elif a>170 and b<=170:
    print("CRASH",b)

elif a>170 and b>170 and c<=170:
    print("CRASH",c)
    
else:
    print("PASS")
    
# 1085
h, b, c, s = map(int, input().split())

result = h*b*c*s
print(round(result/8/1024/1024,1), "MB")



# 1026(백준)
# 안됨. 
n = int(input())

lst_A = [int(x) for x in input().split() if int(x)<=100]
lst_B = [int(x) for x in input().split() if int(x)<=100]


min_list = []

from random import shuffle

for count in range(n*n):
    
    S = 0
    
    shuffle(lst_A)    
    
    for i in range(n):
        
        S+=lst_A[i]*lst_B[i]
    
    min_list.append(S)
    
print(min(min_list))
    