# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:35:17 2020

@author: a0105
"""

# 4651
play_list = [int(x) for i in range(3) for x in input().split()]

n = 4

play_list_split = [play_list[i*n:(i+1)*n] for i in range((len(play_list)+n-1)//n)]

for y_play in play_list_split:
    if y_play.count(0)==1:
        print("A")
    elif y_play.count(0)==2:
        print("B")
    elif y_play.count(0)==3:
        print("C")
    elif y_play.count(0)==4:
        print("D")
    else:
        print("E")


# 1734
name = input()

if len(name)<10:       
    print("welcome!",name)
        
# 4891
student_count = int(input())
score_list = [int(x) for x in input().split() if int(x)>=0 and int(x)<=1000]

print(max(score_list)-min(score_list))