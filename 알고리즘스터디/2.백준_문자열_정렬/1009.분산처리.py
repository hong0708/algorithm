t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    dataList = []
    tempNum = 1
    for i in range(b):
        tempNum *= a
        tempNum %= 10
        if tempNum in dataList:
            break
        dataList.append(tempNum)
    answer = dataList[b % len(dataList) - 1]

    if answer == 0:
        print(10)
    else:
        print(answer)