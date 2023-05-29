def solution(strArr):
    answer = []
    for i, j in enumerate(strArr):
        if i%2 != 0:
            answer.append(j.upper())
        else:
            answer.append(j.lower())
    return answer