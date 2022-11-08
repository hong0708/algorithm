from collections import deque

board = [[0 for _ in range(11)] for _ in range(11)]
visited = [[0 for _ in range(52)] for _ in range(52)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

px = [1, 0, -1, 0, -1, 1, 1, -1]
py = [0, 1, 0, -1, -1, 1, -1, 1]


def check_loc(x, y, board):
    for j in range(8):
        next_x = x + px[j]
        next_y = y + py[j]

        if -1 < next_x < 11 and -1 < next_y < 11:

            if board[next_x][next_y] == 0:
                return True
    else:
        return False


def move_loc(board, start_x, start_y, count, itemX, itemY):
    min_count = 1000000
    visited[start_x][start_y] = 1
    route = deque()
    route.append([start_x, start_y, count])

    while route:
        x, y, now_count = route.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_y == itemY and next_x == itemX:
                min(min_count, count + 1)

            elif -1 < next_x < 53 and -1 < next_y < 53 and not visited[next_x][next_y] and board[next_x][next_y]:
                if check_loc(next_x, next_y, board):
                    visited[next_x][next_y] = 1
                    route.append([next_x, next_y, now_count + 1])

    return min_count


def solution(rectangle, characterX, characterY, itemX, itemY):
    for rec in rectangle:
        for a in range(rec[0], rec[2] + 1):
            for b in range(rec[1], rec[3] + 1):
                board[a][b] = 1

    temp = []
    for i in range(len(board)):
        for j in range(len(board)):
            if not check_loc(i, j, board):
                temp.append([i, j])

    for t in range(len(temp)):
        board[temp[t][0]][temp[t][1]] = 0

    for i in range(len(board)):
        print(board[i])

    answer = move_loc(board, characterX, characterY, 0, itemX, itemY)

    return answer


abc = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]

print(solution(abc, 1, 3, 7, 8))
