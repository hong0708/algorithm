# https://www.acmicpc.net/problem/1389

INF = 1e9

n, m = map(int, input().split())
arr = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
ans = [INF for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            arr[i][j] = 0

for i in range(1, n + 1):  # 중간점
    for j in range(1, n + 1):  # 시작
        for k in range(1, n + 1):  # 끝
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

res = INF
answer = 0
for i in range(1, n + 1):
    if res > sum(arr[i][1:]):
        answer = i
        res = sum(arr[i][1:])
print(answer)