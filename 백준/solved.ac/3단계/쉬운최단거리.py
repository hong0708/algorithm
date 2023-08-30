# https://www.acmicpc.net/problem/14940

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
visited = [[-1 for _ in range(m)] for _ in range(n)]
arr = []

for i in range(n):
    impl = list(map(int, input().split()))
    arr.append(impl)
    for k in range(m):
        if impl[k] == 0:
            visited[i][k] = 0
        if impl[k] == 2:
            a = i
            b = k
            visited[i][k] = 0

d = deque()
d.append([a, b])
while d:
    now = d.popleft()
    x, y = now[0], now[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n and -1 < ny < m:
            if arr[nx][ny] == 0:
                visited[nx][ny] = 0
            elif arr[nx][ny] == 1:
                if visited[nx][ny] > visited[x][y] + 1 or visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    d.append([nx, ny])

for a in visited:
    print(*a)
