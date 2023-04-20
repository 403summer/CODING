def solution(n, k):
    if k-(n//10) >= 0:
        k = k - (n//10)
    else:
        k = 0
    return n * 12000 + k * 2000