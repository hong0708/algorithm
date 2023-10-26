# https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())
arr = []
INF = 1e9
res = [INF for _ in range(k + 1)]
for _ in range(n):
    x = int(input())
    arr.append(x)
    res[x] = 1

for coin in arr:
    if coin <= k:
        res[coin] = 1
    for i in range(coin, k + 1):
        if i - coin > 0:
            res[i] = min(res[i - coin] + 1, res[i])

if res[k] == 0:
    print(-1)
else:
    print(res[k])
