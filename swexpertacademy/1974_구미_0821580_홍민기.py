tc = int(input())
for t in range(tc):
    answer = 1
    arr = [list(map(int, input().split())) for _ in range(9)]

    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in range(9):
            if arr[i][a] in check:
                check[arr[i][a] - 1] = 0
            else:
                answer = 0
    for i in range(9):
        check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in range(9):
            if arr[a][i] in check:
                check[arr[a][i] - 1] = 0
            else:
                answer = 0

    for i in range(0, 9, 3):
        if answer == 0:
            break
        for j in range(0, 9, 3):
            if answer == 0:
                break
            check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for a in range(3):
                for b in range(3):
                    if i + a > 8 or j + b > 8:
                        break
                    if arr[i + a][j + b] in check:
                        check[arr[i + a][j + b] - 1] = 0
                    else:
                        answer = 0
    print("#{} {}".format(t + 1, answer))
