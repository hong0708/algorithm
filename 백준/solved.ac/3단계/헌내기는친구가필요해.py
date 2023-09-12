# https://www.acmicpc.net/problem/21736

import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().rstrip().split())
arr = []
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    arr.append(list(input().rstrip()))


def find(q, w):
    d = deque()
    d.append([q, w])
    ans = 0
    while d:
        now = d.pop()
        x, y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m and arr[nx][ny] != 'X' and not visited[nx][ny]:
                if arr[nx][ny] == 'P':
                    ans += 1
                visited[nx][ny] = True
                d.append([nx, ny])
    return ans


for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            visited[i][j] = True
            res = find(i, j)
if res == 0:
    print('TT')
else:
    print(res)
