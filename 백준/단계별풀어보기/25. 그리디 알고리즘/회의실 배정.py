# https://www.acmicpc.net/problem/1931

n = int(input())
arr = []

for _ in range(n):
    x = list(map(int, input().split()))
    arr.append(x)

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

loc = 0
ans = 0
for i, j in arr:
    if i >= loc:
        ans += 1
        loc = j
print(ans)
