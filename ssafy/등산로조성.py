dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def checkRoute(x, y, hight, count, minus):
    global maxRoute
    if maxRoute < count:
        maxRoute = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if hight > data[nx][ny]:
                visited[nx][ny] = True
                checkRoute(nx, ny, data[nx][ny], count + 1, minus)
            else:
                if minus:
                    for mCount in range(1, k + 1):
                        if (data[nx][ny] - hight + 1) <= mCount and data[nx][ny] - mCount >= 0:
                            visited[nx][ny] = True
                            checkRoute(nx, ny, data[nx][ny] - mCount, count + 1, False)
            visited[nx][ny] = False
    return


# and hight > data[ny][nx] - mCount

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    maxNum = 0
    for c in range(n):
        if maxNum < max(data[c]):
            maxNum = max(data[c])

    maxRoute = 0
    visited = [[False] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if data[a][b] == maxNum:
                visited[a][b] = True
                checkRoute(a, b, maxNum, 1, True)
                visited[a][b] = False

    print("#{} {}".format(tc + 1, maxRoute))
