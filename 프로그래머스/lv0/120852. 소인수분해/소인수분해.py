def solution(n):
    answer = []
    sample = n
    while True:
        for i in range(2,n+1):
            if n%i == 0:
                answer.append(i)
                n = n//i
                break
        a = 1
        for i in answer:
            a = a*i
        if a == sample:
            break
    return sorted(list(set(answer)))