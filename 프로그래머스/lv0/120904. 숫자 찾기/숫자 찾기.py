def solution(num, k):
    if str(num).find(str(k)) >= 0:   
        answer = str(num).find(str(k))+1
    else:
        answer = -1
    return answer