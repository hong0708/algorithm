for t in range(10):
    n = int(input())
    arr = [0] + [list(input().split()) for _ in range(n)]
    for i in range(len(arr) - 1, 0, -1):
        if len(arr[i]) == 4:
            if arr[i][1] == '+':
                arr[i] = [i, float(arr[int(arr[i][2])][1]) + float(arr[int(arr[i][3])][1])]
            elif arr[i][1] == '-':
                arr[i] = [i, float(arr[int(arr[i][2])][1]) - float(arr[int(arr[i][3])][1])]
            elif arr[i][1] == '*':
                arr[i] = [i, float(arr[int(arr[i][2])][1]) * float(arr[int(arr[i][3])][1])]
            else:
                arr[i] = [i, float(arr[int(arr[i][2])][1]) / float(arr[int(arr[i][3])][1])]

    print("#{} {}".format(t + 1, int(arr[1][1])))
