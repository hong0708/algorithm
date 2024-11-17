import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def sink_DFS(x, y, h):
    d = deque()
    d.append([x, y])
    while d:
        x, y = d.popleft()
        for m in range(4):
            nx = x + dx[m]
            ny = y + dy[m]
            if -1 < nx < n and -1 < ny < n and not sink[nx][ny] and arr[nx][ny] > h:
                sink[nx][ny] = True
                d.append([nx, ny])


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for k in range(1, max(map(max, arr))):
    sink = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not sink[i][j]:
                count += 1
                sink[i][j] = True
                sink_DFS(i, j, k)
    ans = max(ans, count)

print(ans)
