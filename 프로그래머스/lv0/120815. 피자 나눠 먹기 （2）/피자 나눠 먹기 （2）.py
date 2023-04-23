def solution(n):
    for i in range(1,60):
        if (6*i)%n == 0:
            answer = i
            break
    return answer