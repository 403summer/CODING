#[BOJ-10845] 큐

from collections import deque

queue = deque()
command = []

N = int(input())
for i in range(N):
    command.append(input())

for i in command:

    if 'push' in i:
        a, b = i.split()
        b = int(b)
        queue.append(b)
    elif 'pop' == i:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' == i:
        print(len(queue))
    elif 'empty' == i:
        if len(queue) == 0:
            print(1)
        else:    
            print(0)
    elif 'front' == i:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' == i:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


