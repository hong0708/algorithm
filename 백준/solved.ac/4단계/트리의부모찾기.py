# https://www.acmicpc.net/problem/11725

n = int(input())
arr = [[] for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]
ans[1] = 1

for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a] += [b]
    arr[b] += [a]

d = [1]
while d:
    now = d.pop()
    for i in arr[now]:
        if not ans[i]:
            ans[i] = now
            d.append(i)

for i in range(2, n + 1):
    print(ans[i])
