# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:56:41 2020

@author: a0105
"""

# 1920
num = int(input())

def dec2bin(n):
    if n < 2:
        return str(n)
    else:
        return dec2bin(n//2) + dec2bin(n%2)
    
print(dec2bin(num))


# 1451

n = int(input())

lst = []

for x in range(n):
    lst.append(int(input()))
    
for i in sorted(lst):
    print(i)
    
# 2055
a, b = map(int,input().split())

a_measure = []
b_measure = []

for i in range(1, a+1):
    if a%i==0:
        a_measure.append(i)
        
for i in range(1, b+1):
    if b%i==0:
        b_measure.append(i)
        
end_lst = a_measure + b_measure

for i in sorted(set(end_lst)):   # 시간초과 발생 
    print(i, end=' ')

