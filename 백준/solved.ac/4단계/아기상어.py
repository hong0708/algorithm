# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

# 가장 위, 가장 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    impls = list(map(int, sys.stdin.readline().split()))
    if 9 in impls:
        k, l = i, impls.index(9)
        impls[l] = 0
    arr.append(impls)


def next_loc(x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dq = deque()
    dq.append([x, y, 0])
    impl = []
    visited[x][y] = True
    while dq:
        a, b, c = dq.popleft()
        for j in range(4):
            nx, ny = a + dx[j], b + dy[j]
            if -1 < nx < n and -1 < ny < n and not visited[nx][ny] and arr[nx][ny] <= bs:
                # 먹을 수 있는 물고기 있는 곳이라면
                if 0 < arr[nx][ny] < bs:
                    impl.append([c + 1, nx, ny])
                # 먹을 수 없거나 그냥 길이라면 그냥 간다.
                else:
                    dq.append([nx, ny, c + 1])
                visited[nx][ny] = True
    return sorted(impl, key=lambda x: (x[0], x[1], x[2]))


loc = deque()
loc.append([k, l, 2, 0, 0])
while loc:
    loc_x, loc_y, bs, e, t = loc.popleft()
    lis = next_loc(loc_x, loc_y)
    if len(lis) == 0:
        print(t)
        break
    nt, n_x, n_y = lis[0]
    arr[n_x][n_y] = 0
    if e + 1 == bs:
        loc.append([n_x, n_y, bs + 1, 0, t + nt])
    else:
        loc.append([n_x, n_y, bs, e + 1, t + nt])
