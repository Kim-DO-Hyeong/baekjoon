from queue import PriorityQueue
import sys

input = sys.stdin.readline

que = PriorityQueue()

n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        if que.empty():
            print(0)
        else:
            print(-que.get())
    else:
        que.put(-num)
