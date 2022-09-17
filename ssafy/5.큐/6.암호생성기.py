from collections import deque

for tc in range(10):
    n = int(input())
    numList = list(list(map(int, input().split())))
    data = deque()

    for i in range(len(numList)):
        data.append(numList[i])

    count = 1
    while True:
        fisrtNum = data.popleft()
        if fisrtNum - count <= 0:
            data.append(0)
            break
        else:
            data.append(fisrtNum - count)
        count += 1
        if count == 6:
            count = 1
    print("#{}".format(tc + 1))
    for z in range(len(data)):
        print(data[z], end=" ")
