def solution(before, after):
    dict_before = {}
    dict_after = {}
    for i in before:
        dict_before[i] = before.count(i)
    for j in after:
        dict_after[j] = after.count(j)
    return int(dict_before == dict_after)