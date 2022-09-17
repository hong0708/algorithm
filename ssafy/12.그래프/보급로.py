from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def tank(x, y):
    time = [[-1] * n for _ in range(n)]
    time[x][y] = 0
    time_q = deque()
    time_q.append((x, y))
    while time_q:
        a, b = time_q.popleft()
        for i in range(4):
            next_x = a + dx[i]
            next_y = b + dy[i]
            if -1 < next_x < n and -1 < next_y < n:
                if time[next_x][next_y] == -1 or time[next_x][next_y] > time[a][b] + arr[next_x][next_y]:
                    time[next_x][next_y] = time[a][b] + arr[next_x][next_y]
                    time_q.append((next_x, next_y))
    return time[n - 1][n - 1]


tc = int(input())
for t in range(tc):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    print("#{} {}".format(t + 1, tank(0, 0)))
