# https://www.acmicpc.net/problem/16933

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def mapping():
    visited = [[[n * m] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][k] = 1

    q = deque()
    q.append([0, 0, k, True])
    while q:
        x, y, c = q.popleft()  # 좌표와 벽을 부술 수 있는 남은 횟수
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y

            if 0 <= tx < n and 0 <= ty < m:
                if mapp[tx][ty] == '1' and c > 0 and visited[x][y][c] + 1 < visited[tx][ty][c - 1]:  # 벽을 한 개 부숨
                    visited[tx][ty][c - 1] = visited[x][y][c] + 1
                    q.append([tx, ty, c - 1])
                    # c를 -1해서 저장
                # 빈 방이라면
                elif mapp[tx][ty] == '0' and visited[x][y][c] + 1 < visited[tx][ty][c]:
                    visited[tx][ty][c] = visited[x][y][c] + 1
                    q.append([tx, ty, c])
    return -1


n, m, k = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(input()))
print(mapping())
