n, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0

n, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0


def go(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < n and check[new_x][new_y]:
            temp = abs(maps[x][y] - maps[new_x][new_y])
            if L <= temp <= R:
                check[new_x][new_y] = False
                stack.append([new_x, new_y])
                go(new_x, new_y)


while True:
    check = [[True] * n for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            stack = []

            if check[i][j]:
                stack.append([i, j])
                check[i][j] = False
                go(i, j)

                if len(stack) > 1:
                    flag = False
                    avg = sum([maps[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        maps[x][y] = avg

    if flag:
        break

    count += 1

print(count)