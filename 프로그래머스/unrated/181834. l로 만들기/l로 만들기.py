def solution(myString):
    answer = []
    for string in myString:
        if ord(string) < 108:
            answer.append('l')
        else:
            answer.append(string)
    return ''.join(answer)