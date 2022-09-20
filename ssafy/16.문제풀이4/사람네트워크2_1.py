t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = arr[0]
    data = []
    INF = int(1e8)
    for i in range(1, len(arr) - n + 1, n):
        data.append(arr[i:i + n])

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                data[i][j] = INF
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    data[i][j] = 0
                else:
                    data[i][j] = min(data[i][j], data[i][k] + data[k][j])
    answer = INF
    for i in range(n):
        count = 0
        for j in range(n):
            count += data[i][j]

        if answer > sum(data[i]):
            answer = sum(data[i])
    print("#{} {}".format(tc, answer))
