# https://www.acmicpc.net/problem/14501

n = int(input())
arr = [[] for _ in range(n)]

ans = [0 for _ in range(n + 1)]

for a in range(n):
    d, w = map(int, input().split())
    arr[a] += [d, w]

before_max = 0
for i in range(n):
    day, warn = arr[i][0], arr[i][1]

    before_max = max(before_max, ans[i])

    if i + day <= n:
        ans[i + day] = max(ans[i + day], before_max + warn)
print(max(ans))
