n = int(input())
f = [0] * (n+1)
f[0] = 0
f[1] = 1
f[2] = 1

cnt = 0
def fib(n):
    global cnt
    if n in [1,2]:
        return 1
    else:
    
        cnt+=1
        return (fib(n - 1) + fib(n - 2))
cnt2 = 0
def fibonacci(n) :
    global cnt2
    for i in range(3,n+1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
        cnt2 +=1
    return f[n]

# fib(n)
print(fibonacci(n))
# print(cnt+1)
print(cnt2)