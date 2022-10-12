tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    data90 = [[0 for _ in range(n)] for _ in range(n)]
    data180 = [[0 for _ in range(n)] for _ in range(n)]
    data270 = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)

    # 90
    for i in range(n):
        for j in range(n):
            data90[i][j] = data[n - j - 1][i]

    # 180
    for i in range(n):
        for j in range(n):
            data180[i][j] = data[n - i - 1][n - j - 1]

    # 270
    for i in range(n):
        for j in range(n):
            data270[i][j] = data[j][n - i - 1]

    print("#{}".format(t))
    for z in range(n):
        for a in range(n):
            print(data90[z][a], end='')
        print(end=' ')
        for b in range(n):
            print(data180[z][b], end='')
        print(end=' ')
        for c in range(n):
            print(data270[z][c], end='')
        print()
