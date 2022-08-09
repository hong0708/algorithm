def check(board, cnt, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                down = 0
                right = 0
                for k in range(i + 1, n):
                    if board[k][j] == 1:
                        down += 1
                    else:
                        break

                for k in range(j + 1, n):
                    if board[i][k] == 1:
                        right += 1
                    else:
                        break

                if down != right:
                    return 'no'

                for x in range(i, i + down + 1):
                    for y in range(j, j + right + 1):
                        if board[x][y] == 1:
                            cnt -= 1
                        else:
                            return 'no'

                if cnt != 0:
                    return 'no'
                return 'yes'


tc = int(input())
for t in range(tc):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        data = list(map(str, input()))
        for j in range(n):
            c = data[j]
            if c == '#':
                board[i][j] = 1
                cnt += 1
            else:
                continue

    result = check(board, cnt, n)

    print("#{} {}".format(t + 1, result))
