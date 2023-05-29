def solution(num_list):
    A = [str(i) for i in num_list if i%2 == 0]
    B = [str(i) for i in num_list if i%2 != 0]
    answer = int(''.join(A)) + int(''.join(B))  
    return answer