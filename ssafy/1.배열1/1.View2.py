for t in range(10):
    arrLen = int(input())
    data = list(map(int, input().split()))

    countView = 0
    for i in range(2, arrLen - 2):
        longBild = max(data[i + 1], data[i + 2], data[i - 1], data[i - 2])

        if data[i] > longBild:
            countView += data[i] - longBild

    print("#{} {}".format(t + 1, countView))
