def solution(array, n):
    array = sorted(array)
    list = []
    for i in array:
        list.append(abs(i-n))
    answer = array[list.index(min(list))]
    return answer