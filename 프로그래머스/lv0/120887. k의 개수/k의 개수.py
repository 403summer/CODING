def solution(i, j, k):
    k_count = 0
    for num in range(i,j+1):
        k_count += str(num).count(str(k))
    return k_count