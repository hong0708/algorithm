# https://www.acmicpc.net/problem/2096

INF = 1e9
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

ans = [[0, INF] for _ in range(3)]
for i in range(3):
    ans[i][0] = arr[0][i]
    ans[i][1] = arr[0][i]

for i in range(1, n):
    a = max(ans[0][0], ans[1][0]) + arr[i][0]
    b = min(ans[0][1], ans[1][1]) + arr[i][0]

    c = max(ans[0][0], ans[1][0], ans[2][0]) + arr[i][1]
    d = min(ans[0][1], ans[1][1], ans[2][1]) + arr[i][1]

    e = max(ans[2][0], ans[1][0]) + arr[i][2]
    f = min(ans[2][1], ans[1][1]) + arr[i][2]

    ans[0][0] = a
    ans[0][1] = b

    ans[1][0] = c
    ans[1][1] = d

    ans[2][0] = e
    ans[2][1] = f

res = [0, INF]
for x, y, in ans:
    res[0] = max(res[0], x)
    res[1] = min(res[1], y)
print(*res)