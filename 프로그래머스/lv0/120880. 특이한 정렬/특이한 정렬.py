def solution(numlist, n):
    answer = []
    
    # 초기조건 리스트에서 n 없애기
    if numlist.count(n):
        answer.append(n)
        numlist.remove(n)
        
    while True:
        # 반복문 종료 조건
        if len(numlist) == 0:
            break
            
        # 편차 제일 작은 값 추출
        for i in numlist:
            if i == numlist[0]:
                min_value = abs(n-i)
            elif abs(n-i) < min_value:  
                min_value = abs(n-i)
        
        # 조건
        if numlist.count(n+min_value) == 1 and numlist.count(n-min_value) == 1:
            answer.append(n+min_value)
            answer.append(n-min_value)
            numlist.remove(n+min_value)
            numlist.remove(n-min_value)
        elif numlist.count(n+min_value) == 1 and numlist.count(n-min_value) == 0:
            answer.append(n+min_value)
            numlist.remove(n+min_value)
        elif numlist.count(n+min_value) == 0 and numlist.count(n-min_value) == 1:
            answer.append(n-min_value)
            numlist.remove(n-min_value)

    return answer