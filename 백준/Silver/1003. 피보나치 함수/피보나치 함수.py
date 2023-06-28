
T = int(input())
list_n = []

for i in range(T):
    s = int(input())
    list_n.append(s)

zero = [1,0]
one = [0,1]

for i in range(2,41):
    zero.append(zero[i-1] + zero[i-2])
    one.append(one[i-1] + one[i-2])

for i in list_n:
    print(zero[i],one[i])
