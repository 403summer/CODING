def solution(a, b):
    # 유한소수 판별 
    answer = 2
    if a == b:
        answer = 1
    elif a%b == 0:
        answer = 1
            
    # 기약분수 만들기
    if a >= b:
        common_num = b  
    else: 
        common_num = a
        
    co_num = []
    for i in range(2, common_num+1):
        if a%i == 0 and b%i == 0:
            co_num.append(i)
    if len(co_num) > 0:
        a = a//max(co_num)
        b = b//max(co_num)
    
    # 소인수분해
    check = []
    for j in range(2, b+1):
        if b%j == 0:
            check.append(j)
    
    check_2 = []
    for k in check:
        if (k%2 == 0 and k/2 != 1) or (k%5 == 0 and k/5 != 1):
            check_2.append(k)
    for z in check_2:
        check.remove(z)
    
    # 유한 소수 판별 2
    if ((2 in check) and len(check) == 1) or ((5 in check) and len(check) == 1) or ((2          in check) and (5 in check) and len(check) == 2):
        answer = 1
            
    return answer