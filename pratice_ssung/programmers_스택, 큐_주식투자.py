

# 주식 가격
# 최종 목표: 가격이 떨어지지 않은 기간은 몇 초 인가
# 입력: prices = [1, 2, 3, 2, 3]
# 출력: [4,3,1,1,0]

# 1초 시점의 가격인 1보다 떨어지는 경우 없으므로 4
# 2초 시점의 가격인 2보다 떨어지는 경우 없으므로 3
# 3초 시점의 가격인 3보다 떨어지는 경우가 1개 있으므로 1
# 4초 시점의 가격인 2보다 떨어지는 경우가 없으므로 1
# 5초 시점 이후에는 기간이 없으므로 0



# 이중 for문 
# 테스트 1 〉	통과 (151.44ms, 18.9MB)
# 테스트 2 〉	통과 (117.94ms, 17.6MB)
# 테스트 3 〉	통과 (188.66ms, 19.5MB)
# 테스트 4 〉	통과 (135.81ms, 18.2MB)
# 테스트 5 〉	통과 (91.25ms, 16.9MB)

prices = [1, 2, 3, 2, 3]


def solution(prices):
    
    answer = [0] * len(prices)
    
    for i in range(len(prices)): # prices 개수 만큼 for문 
        for j in range(i + 1, len(prices)):  # 한 칸씩 밀리면서 비교 
            
            answer[i] += 1

            if prices[i] > prices[j]: # 작은 것이 있으면 break
                break
        
    return answer

solution(prices)

# 스택을 쌓고 크기 비교 후 pop한 다른 사람 풀이 
# 스택으로 생성시 

# 테스트 1 〉	통과 (24.35ms, 18.9MB)
# 테스트 2 〉	통과 (18.08ms, 17.6MB)
# 테스트 3 〉	통과 (27.25ms, 19.5MB)
# 테스트 4 〉	통과 (20.73ms, 18.2MB)
# 테스트 5 〉	통과 (15.08ms, 16.9MB)

def solution_stack(prices):
    
    n = len(prices)
    answer = [0] * n  # 마지막 시점 이후에는 기간이 없으므로 0
    
    stack = []   # list를 이용하여 시점을 담을 stack 구현
    
    for i in range(n):
        # stack 이 존재하고 prices의 top이 그 전에 쌓인 데이터들 보다 크면 반복해서 pop
        # stack[-1]: 스택에서 top을 가리킴. 
        # price에서 
        while stack and prices[stack[-1]] > prices[i]:
            # stack의 마지막 시점
            top = stack.pop()
            answer[top]  = i - top
            
        stack.append(i)  # 시점 저장    # stack 에 0, 1, 3, 4 존재. 
        
    print(stack)
    
    while stack:

        top = stack.pop()
        answer[top] = n - 1 - top  # answer[top]에 가장 마지막 시간 n - i 에서 top을 뺸 시간 저장
            
    return answer

solution_stack(prices)

# deque를 사용하여 풀이 
# 테스트 1 〉	통과 (61.40ms, 18.8MB)
# 테스트 2 〉	통과 (47.74ms, 17.6MB)
# 테스트 3 〉	통과 (78.11ms, 19.5MB)
# 테스트 4 〉	통과 (54.62ms, 18.3MB)
# 테스트 5 〉	통과 (36.62ms, 16.9MB)
prices = [1, 2, 3, 2, 3]

from collections import deque

def solution_deque(prices):
    
    answer = []
    prices = deque(prices)  # 자료형이 deque 로 바뀜.
    
    while prices:
        
        pop_data = prices.popleft()   # 왼쪽부터 pop
        s_time = 0
        
        for i in prices:  # prices의 pop 값이 prices 모든 값과 비교 
            
            if pop_data>i:   # 가격이 떨어지면 멈추고 
                s_time += 1
                
                break
            
            s_time +=1  # 가격이 떨어지지 않았으면 +1
            
        answer.append(s_time)
        
    return answer


# 스택을 이용하여 푸는 방법이 효율성에서 가장 좋았음. 
    

    
    
        
     
    