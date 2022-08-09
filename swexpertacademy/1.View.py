def checkView(x, y):
    for z in range(-2, 3, 1):
        if mapView[x][y + z] == 1:
            return 0
    return 1

for t in range(10):
    arrLen = int(input())
    data = list(map(int, input().split()))
    mapView = [[0 for _ in range(arrLen)] for _ in range(255)]

    for i in range(arrLen):
        for j in range(arrLen):
            if data[j] == 0:
                continue
            else:
                for k in range(data[j]):
                    mapView[254 - k][i] = 1

    countView = 0
    for a in range(255):
        for b in range(arrLen):
            if mapView[a][b] != 0:
                countView += checkView(a, b)

    print("#{} {}".format(t + 1, countView))
