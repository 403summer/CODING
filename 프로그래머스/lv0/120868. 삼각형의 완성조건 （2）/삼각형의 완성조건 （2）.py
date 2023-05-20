def solution(sides):
    sides = sorted(sides)
    answer = 0
    for i in range(1, sides[1]):
        if sides[1] < sides[0]+i:
            answer += 1
    answer += sum(sides) - sides[1]
    return answer