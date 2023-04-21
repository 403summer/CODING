def solution(price):
    import math
    if 100000 <= price < 300000:
        answer = price * 0.95
    elif 300000 <= price < 500000:
        answer = price * 0.90
    elif 500000 <= price:
        answer = price * 0.80
    else:
        answer = price
    return math.trunc(answer)