def solution(n):
    list = []
    for i in range(2,n+1,2):
        if i%2 == 0:
            list.append(i)
    return sum(list)