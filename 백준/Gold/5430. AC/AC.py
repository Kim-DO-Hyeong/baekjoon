from collections import deque

T = int(input())
input_list = []

for k in range(T):
    p = input()
    n = int(input())
    s = input()[1:-1].split(',')
    
    que = deque(s)


    flag = False
    if n == 0:
        que = []

    rev = 0

    for i in p:
        if i == 'R':
            rev +=1
        elif i == 'D' and len(que) == 0:
            flag = True        
            break
        elif i == 'D':
            if rev % 2 == 0:
                que.popleft()
            else:
                que.pop()
    
    if flag : 
        print('error')
    else : 
        if rev % 2!= 0:
            que.reverse()
        
        print("[" + ",".join(que) + "]")
    