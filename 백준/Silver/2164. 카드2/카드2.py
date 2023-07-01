import queue

que =queue.Queue()

n = int(input())

for i in range(1,n+1):
    que.put(i)

for i in range(n-1):
    que.get()
    card = que.get()
    que.put(card)
print(que.get())
