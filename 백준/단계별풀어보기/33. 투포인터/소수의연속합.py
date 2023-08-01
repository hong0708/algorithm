# https://www.acmicpc.net/problem/1644
n = int(input())
ans = 0
arr = [False, False] + [True for _ in range(n)]

for i in range(2, len(arr)):
    if arr[i]:
        for j in range(2 * i, len(arr), i):
            arr[j] = False
prime = []
for i in range(n + 1):
    if arr[i]:
        prime.append(i)

prefix = [0]
for i in range(len(prime)):
    prefix.append(prefix[i] + prime[i])

start, end = 0, 0
while start != len(prefix) and end != len(prefix):
    if end == len(prefix) - 1:
        if prefix[end] - prefix[start] == n:
            ans += 1
            start += 1

        elif prefix[end] - prefix[start] > n:
            start += 1
        else:
            break
    else:
        if prefix[end] - prefix[start] == n:
            ans += 1
            end += 1
        elif prefix[end] - prefix[start] > n:
            start += 1
        elif prefix[end] - prefix[start] < n:
            end += 1
print(ans)
