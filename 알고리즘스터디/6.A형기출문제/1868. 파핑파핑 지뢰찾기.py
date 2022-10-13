# 상 하 좌 우 왼상 왼하 오상 오하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def checkZeroAround(data, aroundItem):
    while aroundItem:
        tempList = aroundItem.pop(0)
        x, y = tempList[0], tempList[1]
        nowCount = 0
        nowAround = []

        # 이미 본것(숫자) 또는 지뢰는 skip
        if data[x][y] != ".":
            continue

        for f in range(8):
            ttx = x + dx[f]
            tty = y + dy[f]
            if -1 < ttx < n and -1 < tty < n:
                if data[ttx][tty] == "*":
                    nowCount += 1
                elif data[ttx][tty] == ".":
                    nowAround.append((ttx, tty))

        data[x][y] = nowCount
        if nowCount == 0:
            aroundItem += nowAround


tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    count = 0

    for _ in range(n):
        temp = list(input())
        data.append(temp)

    for i in range(n):
        for j in range(n):
            canNext = True
            aroundItem = []

            if data[i][j] != ".":
                continue

            for d in range(8):
                tx = i + dx[d]
                ty = j + dy[d]
                if -1 < tx < n and -1 < ty < n:
                    # 지뢰인 경우 skip
                    if data[tx][ty] == "*":
                        canNext = False
                        break
                    else:
                        aroundItem.append([tx, ty])
            # 주변이 다 0이 아니면 짜른다
            if not canNext:
                continue
            count += 1
            data[i][j] = 0
            checkZeroAround(data, aroundItem)

    for nx in range(n):
        for ny in range(n):
            if data[nx][ny] == ".":
                count += 1
    print("#{} {}".format(t, count))
