def solution(array):
    
    # 최빈값 찾기 
    answer = {}
    
    for i in list(set(array)):
        answer[i] = array.count(i)
    
    key = list(answer.keys())
    value = list(answer.values())
    
    # 출력하기
    if value.count(max(value)) > 1:
        return -1
    else:
        return key[value.index((max(value)))]