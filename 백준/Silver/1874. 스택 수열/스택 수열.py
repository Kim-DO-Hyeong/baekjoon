n = int(input())
cnt = 1
arr = []
op = []
flag = False

for i in range(n):
    num = int(input())
    
    while cnt <= num: 
        arr.append(cnt)
        op.append('+')
        cnt +=1

    if arr[-1] == num:
        arr.pop()
        op.append('-')
    else:
        flag = True
        break

if flag == True:
    print('NO')
else:
    for i in op:
        print(i)
