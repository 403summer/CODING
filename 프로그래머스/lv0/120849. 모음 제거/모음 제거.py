def solution(my_string):
    check = ['a', 'e', 'i', 'o', 'u']
    for i in check:
        my_string = my_string.replace(i, '')
    return my_string