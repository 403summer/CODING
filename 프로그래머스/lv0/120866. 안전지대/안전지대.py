def solution(board):
    n = len(board)
    
    for i in range(n):
        if board[i].count(1) >= 1:
            for j in range(n):
                if board[i][j] == 1:
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                                
                            try:
                                if board[x][y] == 0 and x >= 0 and y >= 0:
                                    board[x][y] = 'X'
                            except:
                                pass
    answer = 0
    for k in range(n):
        answer += board[k].count(0)
    print(board)
    return answer