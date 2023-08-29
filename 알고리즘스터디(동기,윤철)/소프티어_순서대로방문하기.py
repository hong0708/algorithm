from collections import deque
from copy import deepcopy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
ans = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[-1 for _ in range(n)] for _ in range(n)]

target = []
for i in range(1, m + 1):
    x, y = map(int, input().split())
    visited[x - 1][y - 1] = i
    target.append([x - 1, y - 1])

visited[target[0][0]][target[0][1]] = 0
d = deque([[target[0], 2, visited]])

while d:
    now = d.popleft()
    impl = deepcopy(now[2])
    x, y = now[0][0], now[0][1]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        # 범위 안에 벽도 아니고 아직 방문하지 않은 곳
        if -1 < nx < n and -1 < ny < n and arr[nx][ny] != 1 and impl[nx][ny] != 0:
            if impl[nx][ny] == -1:
                impl[nx][ny] = 0
                ex = deepcopy(impl)
                d.append([[nx, ny], now[1], ex])
                impl[nx][ny] = -1

            if impl[nx][ny] == now[1]:
                if now[1] == m:
                    ans += 1
                else:
                    impl[nx][ny] = 0
                    ex = deepcopy(impl)
                    d.append([[nx, ny], now[1] + 1, ex])
                    impl[nx][ny] = now[1]

print(ans)
