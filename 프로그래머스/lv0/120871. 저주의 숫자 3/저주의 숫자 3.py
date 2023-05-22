def solution(n):
    num_list = []
    x_num = 0
    
    while True:
        x_num += 1
        if (x_num % 3 != 0) and (str(x_num).count('3') == 0):
            num_list.append(x_num)
        if len(num_list) == n:
            break
    print(num_list)
    return max(num_list)