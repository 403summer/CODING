def solution(A, B):
    if A == B:
        return 0
    
    answer = []
    for i in range(1, len(A)):
        answer.append(A[-i:] + A[:-i])
    print(answer)
    if answer.count(B) >= 1:
        return answer.index(B)+1
    elif answer.count(B) == 0:
        return -1
        