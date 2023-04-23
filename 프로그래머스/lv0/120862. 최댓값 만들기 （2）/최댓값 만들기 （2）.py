def solution(numbers):
    # 0 제거하기
    if numbers.count(0) > 0:
        numbers.remove(0)
    numbers = sorted(numbers)
    
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        answer = numbers[0] * numbers[1]
    else:
        answer = numbers[-1] * numbers[-2]
    return answer