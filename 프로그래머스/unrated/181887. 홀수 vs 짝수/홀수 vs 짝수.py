def solution(num_list):
    answer = 0
    A = []
    B = []
    for i, j in enumerate(num_list):
        if i%2 == 0:
            A.append(j)
        else:
            B.append(j)
    if sum(A) > sum(B): answer = sum(A)
    else: answer = sum(B)
    return answer