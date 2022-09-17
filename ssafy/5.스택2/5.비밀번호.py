for t in range(10):
    tc, data = map(str, input().split())
    data = list(map(int, data))
    isFin = True

    while isFin:
        isFin = False
        for i in range(1, len(data)):
            if data[i - 1] == data[i]:
                targetNum = i - 1
                data.pop(targetNum)
                data.pop(targetNum)
                isFin = True
                break
    data = list(map(str, data))
    print("#{} {}".format(t + 1, "".join(data)))
