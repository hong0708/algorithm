# https://www.acmicpc.net/problem/16724

import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
matrix = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    a = input()
    matrix.append(list(a))

dq = deque()
kind = 1
res = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dq.append([i, j])

            while dq:
                now = dq.popleft()
                x, y = now[0], now[1]
                visited[x][y] = kind

                dir = matrix[x][y]
                if dir == 'D':
                    nx, ny = x + 1, y
                elif dir == 'U':
                    nx, ny = x - 1, y
                elif dir == 'R':
                    nx, ny = x, y + 1
                else:
                    nx, ny = x, y - 1

                if -1 < nx < n and -1 < ny < m:
                    if not visited[nx][ny]:
                        dq.append([nx, ny])
                    elif visited[nx][ny] != kind:
                        kind += 1
                    elif visited[nx][ny] == kind:
                        kind += 1
                        res += 1
print(res)
