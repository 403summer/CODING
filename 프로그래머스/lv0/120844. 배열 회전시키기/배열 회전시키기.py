def solution(numbers, direction):
    list = []
    if direction == "right":
        list.append(numbers[-1])
        list.extend(numbers[:-1])
    else:
        numbers.append(numbers.pop(0))
        list = numbers
    return list