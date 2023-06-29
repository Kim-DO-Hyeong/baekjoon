n = int(input())

info =[]
for i in range(n):
    a = input().split(" ")
    if len(a[2]) <2:
        a[2] = '0'+a[2]
    if len(a[1]) <2:
        a[1] = '0'+a[1]
    info.append([a[0],int(a[3]+a[2]+a[1])])

info.sort(key=lambda x:-x[1])

print(info[0][0])
print(info[-1][0])

