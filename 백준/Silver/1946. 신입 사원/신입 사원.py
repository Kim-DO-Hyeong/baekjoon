
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    input_list = []
    for j in range(N):
        inputs = [int(s) for s in input().split(" ")]
        input_list.append(inputs)

    input_list.sort()

    cnt = 1
    top = 0

    for k in range(1,N):
        if input_list[k][1] < input_list[top][1]:
            top = k
            cnt +=1

    print(cnt)
