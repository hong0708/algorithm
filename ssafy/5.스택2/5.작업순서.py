for tc in range(10):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    route = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
    answer = []

    for i in range(0, len(data), 2):
        route[data[i + 1]][data[i]] = data[i]

    numStack = []
    numOrder = []

    for a in range(1, v + 1):
        if sum(route[a]) == 0:
            numStack.append(a)
            numOrder.append(a)

    while numStack:
        num = numStack.pop()
        for x in range(1, v + 1):
            for y in range(1, v + 1):
                if route[x][y] == num:
                    route[x][y] = 0

        for z in range(1, v + 1):
            if sum(route[z]) == 0:
                if z not in numOrder:
                    numStack.append(z)
                    numOrder.append(z)
    numOrderStr = list(map(str, numOrder))
    print("#{} {}".format(tc + 1, ' '.join(numOrderStr)))
