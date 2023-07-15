import sys
from collections import deque
queue = deque([])

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def push(n):
    n = int(n)
    queue.insert(0, n)
    return n

def pop():
    if empty() == 1:
        return -1
    else:
        popnum = queue[0]
        del queue[0]
        return popnum

def size():
    return len(queue)

def front():
    if empty() == 1: return -1
    else: return queue[0]

def back():
    if empty() == 1: return -1
    else: return queue[len(queue)-1]


queue = []
global cnt

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        n = cmd[1]
        print(push(n))
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'pop':
        print(pop())
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'front':
        print(front())
    elif cmd[0] == 'back':
        print(back())