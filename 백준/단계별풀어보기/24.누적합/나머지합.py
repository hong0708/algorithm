# https://www.acmicpc.net/problem/10986

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p = [0]
div = [1] + [0 for _ in range(m - 1)]
ans = 0

for i in range(n):
    num = (p[i] + arr[i]) % m
    p.append(num)
    div[num] += 1

for i in range(m):
    if div[i] > 0:
        result = div[i] * (div[i] - 1) // 2
        ans += result

print(ans)
