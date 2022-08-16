from collections import deque

data = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
visited = [False] * 9
route = deque()
answer = []
route.append(1)
while route:
    nowNum = route.popleft()
    answer.append(nowNum)
    for i in range(8):
        if data[i][0] == nowNum and visited[data[i][1]] == False:
            route.append(data[i][1])
            visited[data[i][1]] = True

print(answer)
