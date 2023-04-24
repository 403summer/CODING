def solution(num_list, n):
    list_2d = []
    count = len(num_list)//n
    for _ in range(count):
        list_1d = []
        for _ in range(n):
            list_1d.append(num_list.pop(0))
        list_2d.append(list_1d)
    return list_2d