def solution(rsp):
    list = []
    for i in rsp:
        if i == '2':
            list.append('0')
        elif i == '0':
            list.append('5')
        elif i == '5':
            list.append('2')
    return ''.join(list)