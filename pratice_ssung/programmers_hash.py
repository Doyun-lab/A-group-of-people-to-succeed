# -*- coding: utf-8 -*-

# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    
    bucket = 0
    hash_map = {}
    
    for m in participant:
        hash_map[hash(m)] = m
        bucket += int(hash(m))
        
    for n in completion:
        bucket -= int(hash(n))
    
    answer = hash_map[bucket]
    
    return answer

# 전화번호부 
# 정확성: 84.6
# 효율성: 15.4
# 합계: 100.0 / 100.0
def solution(phone_book):
    
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
    
    return answer
    
# 해시 사용
# 정확성: 84.6
# 효율성: 15.4
# 합계: 100.0 / 100.0
def solution_hash(phone_book):

    answer = True
    
    hash_map = {}
    
    for phone_number in phone_book:
        
        hash_map[phone_number] = hash(phone_number)
        
    for phone_number in phone_book:
        
        temp = ""
        
        for number in phone_number:
            
            temp += number
            
            if temp in hash_map and temp != phone_number:
                
                answer = False
                
    return answer
    
