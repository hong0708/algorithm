def solution(board):
    n = len(board)
    m = len(board[0])

    # dp 준비
    maps = [[0] * m for _ in range(n)]
    maps[0] = board[0]
    for i in range(1, n):
        maps[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                maps[i][j] = min(maps[i - 1][j - 1], maps[i][j - 1], maps[i - 1][j]) +1
    answer = 0
    for a in range(n):
        for b in range(m):
            answer = max(answer, maps[a][b])
    return answer ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
