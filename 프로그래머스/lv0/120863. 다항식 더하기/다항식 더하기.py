def solution(polynomial):
    # 항 별로 리스트 만들기
    polynomial = polynomial.split()
    for _ in range(polynomial.count('+')):
        polynomial.remove('+')
    
    # 일차항과 상수항 나누기
    digit = []
    no_digit = []
    for i in polynomial:
        if i.isdigit():
            digit.append(i)
        else:
            no_digit.append(i)
    
    # 일차항 계산하기
    coefficient = 0
    for j in no_digit:
        if len(j) > 1:
            coefficient += int(j[:-1])
        else:
            coefficient += 1
    
    # 상수항 계산하기
    num = 0
    for k in digit:
        num += int(k)
        
    # 출력하기
    if coefficient > 1 and num > 1:
        return str(coefficient)+'x'+' + '+str(num)
    elif coefficient > 1 and num == 0:
        return str(coefficient)+'x'
    elif coefficient == 1 and num >= 1:
        return 'x'+' + '+str(num)
    elif coefficient == 1 and num == 0:
        return 'x'
    elif coefficient == 0 and num >= 1:
        return str(num)
    elif coefficient == 0 and num == 0:
        return '0'