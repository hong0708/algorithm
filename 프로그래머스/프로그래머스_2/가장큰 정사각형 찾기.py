board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
answer = 0
print len(board)
print len(board[0])
max = 0


for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 0:
            continue
        else:
            a = 0
            b = 0
            while True:
                if board[i + a][j] == 1 and i + a + 1 < len(board):
                    a += 1
                elif board[i + a][j] == 0 or i + a + 1 == len(board):
                    break
            while True:
                if board[i][j + b] == 1 and j + b + 1 < len(board[0]):
                    b += 1
                elif board[i][j + b] == 0 or j + b + 1 == len(board[0]):
                    break
            if a > b:
                l = b
            else:
                l = a
            full = True

            for a in range(i, i + l + 1):
                for b in range(j, j + l + 1):
                    if board[a][b] != 1:
                        full = False

            if max < l+1 and full:
                max = l+1


answer = max * max
print answer
