# https://www.acmicpc.net/problem/1012

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())

for _ in range(t):

    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    ans = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                d = deque()
                d.append([i, j])
                arr[i][j] = -1
                while d:
                    impl = d.pop()
                    x, y = impl[0], impl[1]

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if -1 < nx < n and -1 < ny < m and arr[nx][ny] == 1:
                            d.append([nx, ny])
                            arr[nx][ny] = -1
                ans += 1
    print(ans)
