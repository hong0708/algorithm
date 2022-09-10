def checkRoute(now, lastX, lastY, distance):
    global minCount
    if minCount < distance:
        return

    if now == count:
        distance += abs(lastX - home_index[0]) + abs(lastY - home_index[1])

        minCount = min(distance, minCount)
        return

    for i in range(count):
        if visited[i] == False:
            visited[i] = True
            checkRoute(now + 1, client_index[i][0], client_index[i][1],
                       distance + abs(lastX - client_index[i][0]) + abs(lastY - client_index[i][1]))
            visited[i] = False


t = int(input())
for tc in range(1, t + 1):
    count = int(input())
    arr = list(map(int, input().split()))

    client_index = []
    visited = [False for _ in range(count)]
    minCount = 1000

    company_index = []
    home_index = []

    for i in range(0, len(arr), 2):
        client_index.append([arr[i], arr[i + 1]])
    company_index = client_index.pop(0)
    home_index = client_index.pop(0)

    checkRoute(0, company_index[0], company_index[1], 0)
    print("#{} {}".format(tc, minCount))
