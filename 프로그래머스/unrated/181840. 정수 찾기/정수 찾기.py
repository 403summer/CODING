def solution(num_list, n):
    answer = 1
    if num_list.count(n) == 0:
        answer = 0
    return answer