for t in range(10):
    testNum = int(input())
    answer = 0
    data = [list(map(int, input().split())) for _ in range(100)]

    y = data[99].index(2)  # 열
    x = 98  # 행

    while 1:
        if y + 1 < 100 and data[x][y + 1] == 1:
            while y + 1 < 100 and data[x][y + 1] == 1:
                y += 1
            else:
                x -= 1

        elif y - 1 > 0 and data[x][y - 1] == 1:
            while y - 1 > 0 and data[x][y - 1] == 1:
                y -= 1
            else:
                x -= 1
        else:
            x -= 1

        if x == 0:
            break

    print("#{} {}".format(t + 1, y))
