# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:51:07 2020

@author: a0105
"""
# 런타임 에러 발생 
import heapq   # 최소힙 구조로 동작이 기본 

def heap_hot(nums,K):
    
    heap = []
    # heappush: heap에 모든 원소를 담음 
    for value in nums:
        heapq.heappush(heap, value)
        
    count = 0
    
    #while  [x<K for x in heap].count(True) != 0:
    while heap[0]<K:   
        heapq.heappush(heap, heapq.heappop(heap)+ (heapq.heappop(heap)*2))
        
        result = []
    
    # heappop: 힙에 삽입된 원소를 차례대로 꺼내기 
        for i in range(len(heap)):
            result.append(heapq.heappop(heap))
            
        for value in result:
            heapq.heappush(heap, value)
            
        count +=1 

    return count

heap_hot([1, 2, 3, 9, 10, 12], 7)

# 시간 초과 
def heap_hot(nums,K):
    
    heap = []
    # heappush: heap에 모든 원소를 담음 
    for value in nums:
        heapq.heappush(heap, value)
        
    count = 0
    
    #while  [x<K for x in heap].count(True) != 0:
    while heap[0]<K:
        
        if len(heap) > 1:
        
            heapq.heappush(heap, heapq.heappop(heap)+ (heapq.heappop(heap)*2))
            
            count +=1 
    
    # heappop: 힙에 삽입된 원소를 차례대로 꺼내기 
        #for i in range(len(heap)):
        #    result.append(heapq.heappop(heap))
            
        #for value in result:
        #    heapq.heappush(heap, value)
            

    return count

# 성공 
import heapq   # 최소힙 구조로 동작이 기본 

def heap_hot(heap,K):
    
    heapq.heapify(heap)
        
    count = 0
    
    #while  [x<K for x in heap].count(True) != 0:
    while heap[0]<K:
        
        if len(heap) > 1:
        
            heapq.heappush(heap, heapq.heappop(heap)+ (heapq.heappop(heap)*2))
            
            count +=1 
    
        else:
            return -1            

    return count