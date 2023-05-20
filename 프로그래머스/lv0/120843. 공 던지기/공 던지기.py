def solution(numbers, k):
    order = 1 + 2*(k-1)
    if order > len(numbers):
        answer = numbers[order%(len(numbers))-1]
    else:
        answer = numbers[order-1]
    return answer