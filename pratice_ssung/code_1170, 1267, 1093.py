# 1170

a, b, c = map(int, input().split())

print('%d%d'%(a, b),end = '')

if c < 10:
    print(0, end='')
    print(c)   
else:
    print(c)
    
# 1267
n = int(input())

lst = map(int,input().split())

a = 0

for i in lst:
        
    if i % 5 == 0:
        
        a +=i
        
print(a)

# 1093
n = int(input())

lst = map(int,input().split())

lst_0 = [0]*23

for i in lst:
    lst_0[i-1] += 1
    
lst_end = [str(i) for i in lst_0]

print(' '.join(lst_end), end = ' ')