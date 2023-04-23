def solution(my_string):
    list = []
    for i in my_string:
        if i in list:
            pass
        else:
            list.append(i)
    return ''.join(list)