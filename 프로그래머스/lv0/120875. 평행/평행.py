def solution(dots):
    dot_0 = dots[0]
    dot_1 = dots[1]
    dot_2 = dots[2]
    dot_3 = dots[3]
    answer = 0
    
    if (abs(dot_0[1] - dot_1[1])/abs(dot_0[0] - dot_1[0])) == (abs(dot_2[1] - dot_3[1])/abs(dot_2[0] - dot_3[0])):
        answer = 1
    elif (abs(dot_0[1] - dot_2[1])/abs(dot_0[0] - dot_2[0])) == (abs(dot_1[1] - dot_3[1])/abs(dot_1[0] - dot_3[0])):
        answer = 1
    elif (abs(dot_0[1] - dot_3[1])/abs(dot_0[0] - dot_3[0])) == (abs(dot_1[1] - dot_2[1])/abs(dot_1[0] - dot_2[0])):
        answer = 1
            
    return answer