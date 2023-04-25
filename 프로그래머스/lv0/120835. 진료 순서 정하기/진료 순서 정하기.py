def solution(emergency):
    check_list = sorted(emergency)[::-1]
    answer = []
    for i in emergency:
        answer.append(check_list.index(i)+1)
    return answer