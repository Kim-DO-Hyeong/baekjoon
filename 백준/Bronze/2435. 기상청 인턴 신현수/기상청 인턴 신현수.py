N,K = map(int,input().split())
li = list(map(int,input().split()))


li_sum = [-100000] * (N-K+1)

for i in range(N-K+1):
    s = 0
    for j in range(i,i+K):
        s += li[j]
    li_sum[i] = s
    
print(max(li_sum))