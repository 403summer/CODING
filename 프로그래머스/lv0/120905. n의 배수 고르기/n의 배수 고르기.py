def solution(n, numlist):
    list = []
    for i in numlist:
        if i%n == 0:
            list.append(i)
    return list