def solution(score):
    score_list = []
    for i, j in score:
        score_list.append(i+j)
    check_list = sorted(score_list, reverse = True)
    
    answer = []
    for k in score_list:
        answer.append(check_list.index(k) + 1)
    return answer