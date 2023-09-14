# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, sys.stdin.readline().rstrip().split())

arr = [[] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
d = deque()

for i in range(h):
    for j in range(n):
        impl = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(m):
            if impl[k] == 1:
                d.append([j, k, i])
        arr[i].append(impl)
ans = 1

while d:
    x, y, z = d.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if -1 < nx < n and -1 < ny < m and -1 < nz < h and arr[nz][nx][ny] == 0:
            d.append([nx, ny, nz])
            arr[nz][nx][ny] = arr[z][x][y] + 1
            # if arr[nz][nx][ny] > ans:
            #   ans = arr[nz][nx][ny]

can = True
for a in range(h):
    for b in range(n):
        for c in range(m):
            if arr[a][b][c] == 0:
                can = False
                break
            else:
                ans = max(ans, arr[a][b][c])
if can:
    print(ans-1)
else:
    print(-1)
