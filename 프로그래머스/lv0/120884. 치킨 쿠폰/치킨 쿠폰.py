def solution(chicken):
    answer = 0
    bonus = chicken
    while True:
        answer += bonus // 10
        bonus = (bonus // 10) + (bonus % 10)
        if bonus // 10 == 0:
            break
    return answer