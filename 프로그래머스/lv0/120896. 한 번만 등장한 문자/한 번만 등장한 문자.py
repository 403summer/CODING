def solution(s):
    dict = {}
    list = []
    for i in s:
        dict[i] = s.count(i)
    for i,j in dict.items():
        if j == 1:
            list.append(i)
    list = sorted(list)
    return ''.join(list)