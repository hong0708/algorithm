# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
arr = []
res = [0 for _ in range(k + 1)]
for _ in range(n):
    x = int(input())
    arr.append(x)

for coin in arr:
    if coin <= k:
        res[coin] += 1
    for i in range(coin, k + 1):
        if i - coin > 0:
            res[i] += res[i - coin]
print(res[k])
