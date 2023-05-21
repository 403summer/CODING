def solution(id_pw, db):
    dict = {}
    for i, j in db:
        dict[i] = j
    if id_pw[0] in dict.keys():
        if dict.get(id_pw[0]) == id_pw[1]:
            answer = 'login'
        else:
            answer = 'wrong pw'
    else:
        answer = 'fail'        
    return answer