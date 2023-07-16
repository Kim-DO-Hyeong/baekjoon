import sys
input = sys.stdin.readline

dic ={}

n = int(input())

for _ in range(n):
    inp = input().split()
    dic[inp[0]] = inp[1]


li = []
for i in dic:
    if dic[i] == 'enter':
       li.append(i) 

li.sort(reverse=True)

print('\n'.join(map(str,li)))