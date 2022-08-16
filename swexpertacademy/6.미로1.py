from collections import deque

# 하 우 상 좌 보통 결승점은 맨 아래오른쪽이라?
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def checkRoute(i, j):
    global answer
    route = deque()
    route.append([i, j])
    findRoute = True
    while len(route):
        x, y = route.pop()
        for a in range(4):
            mx = x + dx[a]
            my = y + dy[a]
            if -1 < my < 16 and -1 < mx < 16 and data[mx][my] != 1 and visited[mx][my] == False:
                if data[mx][my] == 0:
                    route.append([mx, my])
                    visited[mx][my] = True
                if data[mx][my] == 3:
                    answer = 1
                    route.clear()
                    break


for tc in range(10):
    n = input()
    data = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    answer = 0
    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                checkRoute(i, j)
                print("#{} {}".format(tc + 1, answer))
                break
