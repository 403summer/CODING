def solution(spell, dic):
    dict = {}
    answer = 2
    for i in spell:
        dict[i] = spell.count(i)
    for j in dic:
        dict2 = {}
        for k in j:
            dict2[k] = j.count(k)
        if dict == dict2:
            answer = 1
            break
    return answer