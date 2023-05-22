def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        difference = common[1] - common[0]
        answer = common[-1] + difference
    else:
        ratio = common[1] / common[0]
        answer = common[-1] * ratio
    return answer