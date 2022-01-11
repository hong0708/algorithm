from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
q = deque()


def wall(x):
    if x == 3:
        virus()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0


def virus():
    global answer
    w = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if w[i][j] == 2: q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])
    cnt = 0
    for i in w: cnt += i.count(0)
    answer = max(answer, cnt)


wall(0)
print(answer)
