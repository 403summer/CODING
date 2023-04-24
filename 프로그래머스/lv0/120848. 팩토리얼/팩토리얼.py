def solution(n):
    result = 0
    number = 1
    while True:
        result += 1
        number = number * result
        if number <= n < number*result+1:
            break
    return result
