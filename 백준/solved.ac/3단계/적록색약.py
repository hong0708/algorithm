# https://www.acmicpc.net/problem/10026

from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
arr = []
visited = [[False for _ in range(n)] for _ in range(n)]
ans = [0, 0]
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))


def find(a, b, c):
    d = deque()
    d.append([a, b])
    visited[a][b] = True
    while d:
        now = d.pop()
        x, y, = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n and not visited[nx][ny] and arr[nx][ny] == c:
                visited[nx][ny] = True
                d.append([nx, ny])


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            find(i, j, arr[i][j])
            ans[0] += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            find(i, j, arr[i][j])
            ans[1] += 1

print(*ans)
