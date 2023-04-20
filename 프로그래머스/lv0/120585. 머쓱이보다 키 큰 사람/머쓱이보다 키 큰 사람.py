def solution(array, height):
    list = []
    for i in array:
        if i > height:
            list.append(i)
    return len(list)