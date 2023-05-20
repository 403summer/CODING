def solution(my_str, n):
    share = len(my_str) // n
    
    if len(my_str) % n == 0:
        remainder = 0
    else:
        remainder = len(my_str) % n
    
    list = []
    for i in range(share):
        list.append(n)
    if remainder > 0:
        list.append(remainder)
    
    answer = []
    start = 0
    finish = n
    for j in list:
        answer.append(my_str[start:finish])
        start += j
        finish += j
    return answer