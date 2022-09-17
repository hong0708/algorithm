from collections import deque

for tc in range(10):
    visited = [False] * 101
    nextNums = []
    turn = []
    route = deque()
    n, start = map(int, input().split())
    numList = list(map(int, input().split()))
    data = []
    for j in range(0, n, 2):
        data.append([numList[j], numList[j + 1]])

    route.append(start)
    while route:
        nowNum = route.popleft()
        #turn.append(nowNum)
        visited[nowNum] = True
        for i in range(len(data)):
            if data[i][0] == nowNum and visited[data[i][1]] == False:
                # route.append(data[i][1])
                visited[data[i][1]] = True
                nextNums.append(data[i][1])
        if len(route) == 0 and len(nextNums) != 0:
            for a in range(len(nextNums)):
                route.append(nextNums[a])
            turn = nextNums
            nextNums = []
    print()
    print("#{} {}".format(tc + 1, max(turn)))
