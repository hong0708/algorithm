for t in range(10):
    dumpCount = int(input())
    data = list(map(int, input().split()))

    for _ in range(dumpCount):
        minLenLoc = data.index(min(data))
        maxLenLoc = data.index(max(data))
        data[minLenLoc] += 1
        data[maxLenLoc] -= 1

    answer = max(data) - min(data)
    print("#{} {}".format(t + 1, answer))
