from queue import PriorityQueue

n = int(input())

que = PriorityQueue()

for i in range(n):
    s = int(input())
    que.put(s)

result = 0

if n == 1:
    print(0)
else: 
    for i in range(n-1):
        pre = que.get()
        cur = que.get()

        result += pre + cur

        que.put(pre + cur)
    print(result)
