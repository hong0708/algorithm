# s일때 위쪽에서 아래 방향으로가 시작 and 시계방향 순서
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    answer = []
    w = len(grid[0])
    h = len(grid)

    # 위쪽에서 아래 방향으로가 시작 and 시계방향 순서
    r = {0: 1, 1: 2, 2: 3, 3: 0}
    l = {0: 3, 1: 0, 2: 1, 3: 2}

    # 각 위치에서 네방향 다 돈것인지
    case = [[[False] * 4 for _ in range(w)] for _ in range(h)]

    # 모든 점에서 모든 방향으로 출발
    for x in range(h):
        for y in range(w):
            for i in range(4):
                # 이미 이동한 적 있는 방향은 판단 X
                if case[x][y][i]:
                    continue

                count = 0
                nowX, nowY, nowD = x, y, i

                while True:
                    case[nowX][nowY][nowD] = True
                    count += 1

                    if grid[nowX][nowY] == 'R':
                        nowD = r[nowD]
                    elif grid[nowX][nowY] == 'L':
                        nowD = l[nowD]

                    nowX = (nowX + dx[nowD]) % h
                    nowY = (nowY + dy[nowD]) % w
                    if nowX == x and nowY == y and nowD == i:
                        break
                answer.append(count)
    answer.sort()
    return answer
