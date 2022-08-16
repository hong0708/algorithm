def bingo():
    global count

    zCount = 0
    for a in range(0, 5):
        if data[a][a] == 0:
            zCount += 1
    if zCount == 5:
        bingoList[10] = 1

    zCount = 0
    for a in range(0, 5):
        if data[4 - a][a] == 0:
            zCount += 1
    if zCount == 5:
        bingoList[11] = 1

    for a in range(0, 5):
        zCount = 0
        for b in range(0, 5):
            if data[a][b] == 0:
                zCount += 1
        if zCount == 5:
            bingoList[a] = 1

    for a in range(0, 5):
        zCount = 0
        for b in range(0, 5):
            if data[b][a] == 0:
                zCount += 1
        if zCount == 5:
            bingoList[a + 5] = 1


def check(a):
    for x in range(5):
        for y in range(5):
            if data[x][y] == a:
                data[x][y] = 0


count = 0
answer = 0
data = list(list(map(int, input().split())) for _ in range(5))

bingoList = [0] * 12

for i in range(5):
    numList = list(map(int, input().split()))
    for j in range(5):
        check(numList[j])
        bingo()
        answer += 1
        if sum(bingoList) >= 3:
            print(answer)
            break
    if sum(bingoList) >= 3:
        break
