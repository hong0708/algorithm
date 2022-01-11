def BW_board(y, x, chess_board):
    count1 = 0
    count2 = 1
    count = 0
    before_color = chess_board[y][x]
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (j - x) % 2 == 0 and before_color != chess_board[i][j]:
                count1 += 1
            if (j - x) % 2 != 0 and before_color == chess_board[i][j]:
                count1 += 1

            if (j - x) % 2 == 0 and before_color == chess_board[i][j]:
                count2 += 1
            if (j - x) % 2 != 0 and before_color != chess_board[i][j]:
                count2 += 1
        if before_color == "W":
            before_color = "B"
        else:
            before_color = "W"
    return min(count2, count1)


N, M = map(int, input().split())
min_count = 64
count = 0
chess_borad = [0 for _ in range(N)]
for i in range(N):
    chess_borad[i] = list(map(str, input()))

for y in range(N - 7):
    for x in range(M - 7):
        count = BW_board(y, x, chess_borad)
        if min_count > count:
            min_count = count
print(min_count)
