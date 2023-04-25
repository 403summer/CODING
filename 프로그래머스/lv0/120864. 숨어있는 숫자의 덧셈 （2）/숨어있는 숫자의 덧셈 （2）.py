def solution(my_string):
    # 숫자 추출
    import re
    p = re.compile('[0-9]+')
    list = p.findall(my_string)
    
    # 더하기
    answer = 0
    for i in list:
        answer += int(i)
    return answer