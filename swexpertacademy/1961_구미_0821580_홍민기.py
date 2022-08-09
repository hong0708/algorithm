tc = int(input())
for t in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    roundArr = [[0 for _ in range(n)] for _ in range(n)]
    arr90 = [[0 for _ in range(n)] for _ in range(n)]
    arr180 = [[0 for _ in range(n)] for _ in range(n)]
    arr270 = [[0 for _ in range(n)] for _ in range(n)]

    for a in range(3):
        for i in range(0, n):
            for j in range(0, n):
                roundArr[i][j] = arr[n - j - 1][i]
        if a == 0:
            for i in range(n):
                for j in range(n):
                    arr90[i][j] = roundArr[i][j]
                    arr[i][j] = roundArr[i][j]
        elif a == 1:
            for i in range(n):
                for j in range(n):
                    arr180[i][j] = roundArr[i][j]
                    arr[i][j] = roundArr[i][j]
        else:
            for i in range(n):
                for j in range(n):
                    arr270[i][j] = roundArr[i][j]
                    arr[i][j] = roundArr[i][j]

    print("#{}".format(t + 1))
    for i in range(n):
        for a in range(n):
            print(arr90[i][a], end="")
        print(end=' ')
        for b in range(n):
            print(arr180[i][b], end='')
        print(end=' ')
        for c in range(n):
            print(arr270[i][c], end='')
        print(sep='\n')