def solution(myString, pat):
    answer = 0
    list = []
    for i in myString:
        if i == 'A':
            list.append('B')
        elif i == 'B':
            list.append('A')
    if ''.join(list).count(pat): answer = 1
    return answer