def solution(myString, pat):
    answer = 0
    if myString.upper().count(pat.upper()): answer = 1
    return answer