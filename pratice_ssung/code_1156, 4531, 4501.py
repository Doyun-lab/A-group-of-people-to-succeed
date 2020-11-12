# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:47:11 2020

@author: a0105
"""
# 1156
x=int(input())

if(x%2==1):
    print("odd")
else:
    print("even")

# 4531
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

num_list = [num1, num2, num3, num4, num5]

print(int(sum(num_list)/len(num_list)))
print(sorted(num_list)[len(sorted(num_list))//2])

# 4501
num_list = [input() for i in range(0,7)]

print(sorted(num_list)[6])
print(sorted(num_list)[5])

