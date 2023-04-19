def solution(numer1, denom1, numer2, denom2):
    # 통분
    if denom1 != denom2:
        x = denom1
        y = denom2
        denom1 = denom1 * y
        numer1 = numer1 * y
        denom2 = denom2 * x
        numer2 = numer2 * x

        numer = numer1 + numer2
        denom = denom1
    else:
        numer = numer1 + numer2
        denom = denom1
        
    # 약수 구하기
    def divisor(s):
        list = [1,s]
        for i in range(1, 1000):
            if s % i == 0:
                list.append(i)
                list.append(s/i)
        return list
    A = divisor(numer)
    B = divisor(denom)
    
    # 최대공약수 구하기
    co_divisor = []
    for i in A:
        for j in B:
            if i == j:
                co_divisor.append(i)
    max_divisor = max(co_divisor)
    
    return int(numer/max_divisor), int(denom/max_divisor)