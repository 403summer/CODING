def solution(lines):
    dict = {}
    for i, j in lines:
        for num in range(i, j):
            dict[num] = 0
    for i, j in lines:
        for num in range(i, j):
            dict[num] += 1
            
    answer = 0
    for k in list(dict.values()):
        if k > 1:
            answer += 1
    return answer