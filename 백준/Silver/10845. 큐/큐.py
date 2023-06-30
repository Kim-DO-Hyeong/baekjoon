
a=[]

def push(x):
    a.append(x)

def pop():
    if len(a) == 0:
        print(-1)
    else:
        print(a[0])
        a.remove(a[0])

def size():
    print(len(a))

def front():
    if len(a) == 0:
        print(-1)
    else:
        print(a[0])
    

def back():
    if len(a) == 0:
        print(-1)
    else:
        print(a[-1])
def empty():
    if len(a) == 0:
        print(1)
    else:
        print(0)


n = int(input())

output  = []

for i in range(n):
    s = input()
    s_arr = s.split(" ")
    output.append(s_arr)

for i in output:
    if i[0] == 'push':
        push(int(i[1]))
    elif i[0] == 'front':
        front()
    elif i[0] == 'back':
        back()
    elif i[0] == 'size':
        size()
    elif i[0] == 'empty':
        empty()
    elif i[0] == 'pop':
        pop()