#[BOJ-10828] 스택

stack = []
result = []

N = int(input())
for i in range(N):
    stack.append(input())

for i in stack:

    if 'push' in i:
        a, b = i.split()
        b = int(b)
        result.append(b)
    elif 'pop' == i:
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif 'size' == i:
        print(len(result))
    elif 'empty' == i:
        if len(result) == 0:
            print(1)
        else:    
            print(0)
    elif 'top' == i:
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
