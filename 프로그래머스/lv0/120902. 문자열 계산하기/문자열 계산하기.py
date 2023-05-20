def solution(my_string):
    my_string = my_string.split()
    number = []
    pl_mi = []
    
    for i in my_string:
        if i.isdigit():
            number.append(int(i))
        else:
            pl_mi.append(i)
    
    answer = number.pop(0) 
    for j in pl_mi:
        if j == '+':
            answer += number.pop(0)
        else:
            answer -= number.pop(0)
    return answer