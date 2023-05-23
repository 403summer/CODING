def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    
    for i in can:
        for j in range(len(babbling)):
            babbling[j] = babbling[j].replace(i,' ')
    answer = [i.replace(' ', '')for i in babbling].count('')
    return answer