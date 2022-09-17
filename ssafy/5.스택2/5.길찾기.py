def destination(a):
    global answer
    roadStack = []
    roadStack.append(a)

    while roadStack:
        num = roadStack.pop()

        if num == 99:
            answer = 1
            return
        else:
            if roadData1[num] != -1:
                roadStack.append(roadData1[num])
            if roadData2[num] != -1:
                roadStack.append(roadData2[num])
    return


for tc in range(10):
    n, roadCount = map(int, input().split())
    data = list(map(int, input().split()))
    answer = 0
    roadData1 = [-1] * 100
    roadData2 = [-1] * 100

    for i in range(0, len(data), 2):
        if roadData1[data[i]] == -1:
            roadData1[data[i]] = data[i + 1]
        else:
            roadData2[data[i]] = data[i + 1]

    destination(0)
    print("#{} {}".format(tc + 1, answer))
