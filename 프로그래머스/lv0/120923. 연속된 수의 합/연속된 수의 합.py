def solution(num, total):
    start = (total // num) - num
    while True:
        start += 1
        result = []
        for i in range(start, start + num):
            result.append(i)
        if sum(result) == total:
            answer = result
            break
        
    return answer