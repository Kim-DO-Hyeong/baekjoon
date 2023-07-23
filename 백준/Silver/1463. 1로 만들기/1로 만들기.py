n = int(input())

if n == 1:
    print(0)
    exit()

if n < 4 :
    print(1)
    exit()

D =[]
for i in range(n+1):
    line = [1000000,1000000,1000000,1000000]
    D.append(line)

D[2][3] = 1
D[3][3] = 1

for i in range(4,n+1):
    if i % 3 == 0:
        D[i][0] = D[i//3][3]
    if i % 2 == 0:
        D[i][1] = D[i//2][3]
    
    D[i][2] = D[i-1][3]

    D[i][3] = min([D[i][0],D[i][1],D[i][2]]) +1

print(D[n][3])