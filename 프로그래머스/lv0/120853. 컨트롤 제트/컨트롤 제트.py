def solution(s):
    s = s.split()
    while True:        
        if s.count('Z') >= 1:
            num = s.index('Z')
            s.pop(num)
            s.pop(num-1)
        elif s.count('Z') == 0:
            break
    
    if len(s) == 0:
        answer = 0
    else:
        answer = sum(map(int, s))

    return answer 