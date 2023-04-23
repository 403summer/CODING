def solution(my_string):
    list = []
    for i in my_string:
        if i.islower():
            list.append(i.upper())
        else:
            list.append(i.lower())
    return ''.join(list)