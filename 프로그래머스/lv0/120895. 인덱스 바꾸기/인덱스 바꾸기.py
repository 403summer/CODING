def solution(my_string, num1, num2):
    A = my_string[num1]
    B = my_string[num2]
    my_string = list(my_string)
    my_string[num1] = B
    my_string[num2] = A
    return ''.join(my_string)