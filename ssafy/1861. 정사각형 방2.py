from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def checkRoute(x, y, count):
    nextNums = deque([(x, y)])
    while nextNums:
        x = nextNums[0][0]
        y = nextNums[0][1]
        nextNums.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] - data[x][y] == 1:
                    count += 1
                    nextNums.append((nx, ny))
    return count


t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    maxRoute = 0
    minNum = data[0][0]

    for a in range(n):
        for b in range(n):
            nowRoute = checkRoute(a, b, 1)
            if nowRoute > maxRoute:
                maxRoute = nowRoute
                minNum = data[a][b]
            elif nowRoute == maxRoute:
                if minNum > data[a][b]:
                    minNum = data[a][b]

    print("#{} {} {}".format(tc + 1, minNum, maxRoute))
