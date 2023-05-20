def solution(dots):
    x_list = []
    y_list = []
    for i in dots:
        x_list.append(i[0])
        y_list.append(i[1])
    x = max(x_list) - min(x_list)    
    y = max(y_list) - min(y_list)
    return x*y