# https://www.acmicpc.net/problem/16933

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def mapping():
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][k] = True

    q = deque()
    q.append([0, 0, k, True, 1])
    while q:
        x, y, c, day, ans = q.popleft()  # 좌표와 벽을 부술 수 있는 남은 횟수
        if x == n - 1 and y == m - 1:
            return ans
        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y

            if 0 <= tx < n and 0 <= ty < m and not visited[tx][ty][c]:
                # 빈 방이라면
                if mapp[tx][ty] == '0':
                    visited[tx][ty][c] = True
                    q.append([tx, ty, c, not day, ans + 1])

                if mapp[tx][ty] == '1' and c > 0:  # 벽을 한 개 부숨
                    if day:
                        visited[tx][ty][c - 1] = True
                        q.append([tx, ty, c - 1, not day, ans + 1])
                    # c를 -1해서 저장
                    else:
                        q.append([x, y, c, not day, ans + 1])
    return -1


n, m, k = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(input()))
print(mapping())
