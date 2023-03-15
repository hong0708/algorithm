from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    answer = []
    visited = []
    impl = []

    for i in maps:
        impl.append(list(i))
        visited.append([False for _ in range(len(list(i)))])

    for i in range(len(impl)):
        for j in range(len(impl[0])):
            if impl[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                q = deque()
                q.append([i, j])
                total = 0
                while q:
                    now = q.pop()
                    x = now[0]
                    y = now[1]
                    total += int(impl[x][y])
                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if -1 < nx < len(impl) and -1 < ny < len(impl[0]) and impl[nx][ny] != 'X' and not visited[nx][
                            ny]:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                answer.append(total)
            else:
                visited[i][j] = True
    if len(answer)== 0:
        return [-1]
    else:
        return sorted(answer)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
