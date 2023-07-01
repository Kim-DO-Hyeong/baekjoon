
import sys
a=[]
def push(x):
    a.append(x)

def pop():
    if len(a) == 0:
        print(-1)
    else:
        print(a.pop(-1))

def size():
    print(len(a))

def empty():
    if len(a) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(a) == 0:
        print(-1)
    else:
        print(a[-1])

n = int(sys.stdin.readline())

for s in range(n):
    command = sys.stdin.readline()
    i = command.split()
    if i[0] == 'push':
        push(int(i[1]))
    elif i[0] == 'size':
        size()
    elif i[0] == 'empty':
        empty()
    elif i[0] == 'pop':
        pop()
    elif i[0] == 'top':
        top()