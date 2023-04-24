def solution(n):
    point = 0
    result = 1
    while True:
        point += 1
        result = result * point
        if result <= n < result*point+1:
            print(result)
            break
    return point