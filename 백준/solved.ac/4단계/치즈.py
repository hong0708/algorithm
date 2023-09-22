# https://www.acmicpc.net/problem/2638

from collections import deque
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
c = 0
day = 0
for i in range(n):
    impl = list(map(int, input().split()))
    matrix[i] += impl
    c += sum(impl)


def is_air(q, w):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[q][w] = True

    dq = deque()
    dq.append([q, w])
    while dq:
        now = dq.popleft()
        x, y = now[0], now[1]
        if x == 0 or x == n or y == 0 or y == m:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m and matrix[nx][ny] == 0 and not visited[nx][ny]:
                dq.append([nx, ny])
                visited[nx][ny] = True
    return False


while c != 0:
    day += 1
    arr = deepcopy(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                check = []
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if -1 < nx < n and -1 < ny < m and matrix[nx][ny] == 0:
                        check.append([nx, ny])
                if len(check) >= 2:
                    air_count = 0
                    for a, b in check:
                        if is_air(a, b):
                            air_count += 1
                    if air_count >= 2:
                        arr[i][j] = 0
                        c -= 1
    matrix = deepcopy(arr)
print(day)
