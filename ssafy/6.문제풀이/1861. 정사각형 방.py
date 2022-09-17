dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def checkRoute(x, y, num, count):
    global maxRoute
    global minNum
    if maxRoute < count:
        maxRoute = count
        minNum = num
    elif maxRoute == count:
        if num < minNum:
            minNum = num

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
            if data[nx][ny] - data[x][y] == 1:
                visited[nx][ny] = True
                checkRoute(nx, ny, num, count + 1)
            visited[nx][ny] = False


t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    maxRoute = 0
    minNum = data[0][0]
    visited = [[False] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            visited[a][b] = True
            checkRoute(a, b, data[a][b], 1)
            visited[a][b] = False
    print("#{} {} {}".format(tc + 1, minNum, maxRoute))
