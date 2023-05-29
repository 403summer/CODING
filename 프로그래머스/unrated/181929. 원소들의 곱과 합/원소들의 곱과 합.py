def solution(num_list):
    temp = 1
    for i in num_list:
        temp *= i
    
    answer = 0
    if temp < sum(num_list)**2: answer = 1
    return answer