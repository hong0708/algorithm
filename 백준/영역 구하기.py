import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

ans = 0
ans_list = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(k):
    a, b, x, y = map(int, input().split())
    for j in range(a, x):
        for k in range(b, y):
            arr[k][j] = 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            d = deque()
            d.append([i, j])
            visited[i][j] = True
            s = 1
            ans += 1
            while d:
                x, y = d.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if -1 < nx < m and -1 < ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                        visited[nx][ny] = True
                        d.append([nx, ny])
                        s += 1
            ans_list.append(s)
print(ans)
ans_list.sort()
print(" ".join(map(str, ans_list)))
