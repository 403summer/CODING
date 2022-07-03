#[기초-리스트] 설탕과자 뽑기

h, w = map(int,input().split())

list = [[0 for i in range(h)] for i in range(w)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int,input().split())
    for j in range(l):
        if d == 0:
            list[x+j][y] = 1
        else:
            list[x][y+j] = 1

for i in range(h):
    for j in range(w):
        if j == h:
            print(list[i][j])
        else:
            print(list[i][j], end=' ')
