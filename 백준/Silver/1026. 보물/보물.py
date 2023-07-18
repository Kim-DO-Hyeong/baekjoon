n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

li1.sort()
li2.sort(reverse=True)

s = 0

for i in range(n):
    s += li1[i] * li2[i]

print(s)