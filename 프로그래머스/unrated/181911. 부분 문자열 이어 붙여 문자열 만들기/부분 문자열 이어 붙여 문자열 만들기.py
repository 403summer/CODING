def solution(my_strings, parts):
    answer = []
    for i, j in zip(my_strings, parts):
        start, end = j
        answer.append(i[start:end+1])
    return ''.join(answer)