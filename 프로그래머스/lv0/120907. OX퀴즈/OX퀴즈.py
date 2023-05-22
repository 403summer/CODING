def solution(quiz):
    answer = []
    for i in quiz:
        formula = i.split()
        if formula[1] == '+':
            if int(formula[0]) + int(formula[2]) == int(formula[-1]):
                answer.append('O')
            else:
                answer.append('X')
        elif formula[1] == '-':
            if int(formula[0]) - int(formula[2]) == int(formula[-1]):
                answer.append('O')
            else:
                answer.append('X')
    return answer