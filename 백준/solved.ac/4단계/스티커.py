# https://www.acmicpc.net/problem/9465

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    ans = [[0 for _ in range(n + 1)] for _ in range(3)]
    result = 0

    for i in range(1, n + 1):
        for j in range(3):
            if j == 0:
                ans[j][i] = max(ans[1][i - 1], ans[2][i - 1]) + arr[j][i - 1]
            elif j == 1:
                ans[j][i] = max(ans[0][i - 1], ans[2][i - 1]) + arr[j][i - 1]
            else:
                ans[j][i] = max(ans[0][i - 1], ans[1][i - 1], ans[2][i - 1])
            result = max(result, ans[j][i])
    print(result)
