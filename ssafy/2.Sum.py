for t in range(10):
    testNum = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))

    sumNum = []
    for i in range(100):
        length = 0
        for j in range(100):
            length += data[i][j]
        sumNum.append(length)

    for i in range(100):
        width = 0
        for j in range(100):
            width += data[j][i]
        sumNum.append(width)

    crossLeft = 0
    for i in range(100):
        crossLeft += data[i][i]
    sumNum.append(crossLeft)

    crossRight = 0
    for i in range(100):
        crossRight += data[99 - i][i]
    sumNum.append(crossRight)

    answer = max(sumNum)
    print("#{} {}".format(t + 1, answer))
