def solution(keyinput, board):
    x = 0
    y = 0
    
    for i in keyinput:
        if i == 'right':
            if -(board[0]//2) < x < board[0]//2:
                x += 1
            elif x == -(board[0]//2):
                x += 1
            elif x == board[0]//2:
                pass
        elif i == 'left':
            if -(board[0]//2) < x < board[0]//2:
                x -= 1
            elif x == board[0]//2:
                x -= 1
            elif -(board[0]//2) == x:
                pass
        elif i == 'up':
            if -(board[1]//2) < y < board[1]//2:
                y += 1
            elif -(board[1]//2) == y:
                y += 1
            elif y == board[1]//2:
                pass
        elif i == 'down':
            if -(board[1]//2) < y < board[1]//2:
                y -= 1
            elif y == board[1]//2:
                y -= 1
            elif -(board[1]//2) == y:
                pass
    if board[0] == 0:
        x = 0
    if board[1] == 0:
        y = 0
    return [x,y]