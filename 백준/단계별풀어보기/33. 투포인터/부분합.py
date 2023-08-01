# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
ans = n + 1
arr = list(map(int, input().split()))
prefix = [0]

for i in range(n):
    prefix.append(prefix[i] + arr[i])

start, end = 0, 0

while end != n + 1 and start != n + 1:
    if end == n:
        if prefix[n] - prefix[start] >= s:
            ans = min(end - start, ans)
            start += 1
        else:
            break
    else:
        if prefix[end] - prefix[start] >= s:
            ans = min(end - start, ans)
            start += 1
        else:
            end += 1

if ans == n + 1:
    print(0)
else:
    print(ans)
