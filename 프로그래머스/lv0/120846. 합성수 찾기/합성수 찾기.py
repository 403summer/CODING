def solution(n):
    list = [] # 합성수 리스트
    for i in range(1, n+1):
        counter = 0
        for j in range(1, i+1):
            if i%j == 0:
                counter += 1
        if counter >= 3:
            list.append(i)
    return len(list)