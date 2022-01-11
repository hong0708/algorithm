import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def can_go(board, x, y):
    positions = []
    direction = board[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= board[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions


def find_fish(board, index):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == index:
                return (i, j)
    return None


def next_fish(board, now_sh_x, now_sh_y):
    for i in range(1, 17):
        position = find_fish(board, i)
        if position is None: continue

        x, y = position[0], position[1]
        arrow = board[x][y][1]  # 방향

        for j in range(8):
            nx, ny = x + dx[arrow], y + dy[arrow]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == now_sh_x and ny == now_sh_y):  # 공간의 경계, 상어 있는 칸 확인
                    # 값 교체
                    a = board[x][y][0]
                    board[x][y][0] = board[nx][ny][0]
                    board[nx][ny][0] = a

                    a = board[x][y][1]
                    board[x][y][1] = board[nx][ny][1]
                    board[nx][ny][1] = a

                    #board[x][y][0], board[nx][ny][0] = board[nx][ny][0], board[x][y][0]
                    #board[x][y][1], board[nx][ny][1] = board[nx][ny][1], arrow
                    break
            arrow = (arrow + 1) % 8


def dfs(board1, x, y, total):
    global answer
    board = copy.deepcopy(board1)

    number = board[x][y][0]
    board[x][y][0] = -1

    next_fish(board, x, y)
    can_next = can_go(board, x, y)
    answer = max(answer, total + number)

    for next_x, next_y in can_next:
        dfs(board, next_x, next_y, total + number)


temp = [list(map(int, input().split())) for _ in range(4)]
board = [[None] * 4 for _ in range(4)]
# 배열을 다루기 쉽게 [값, 방향] 형태로 바꾼다.
for i in range(4):
    for j in range(4):
        board[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1]
print(temp)
print(board)

answer = 0
dfs(board, 0, 0, 0)

print(answer)
