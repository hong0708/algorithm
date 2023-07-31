# https://www.acmicpc.net/problem/2470

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n - 1
ans = [arr[start], arr[end]]
z = abs(arr[start] + arr[end])

while start < end:
    now = arr[start] + arr[end]
    if abs(now) < z:
        ans[0], ans[1] = arr[start], arr[end]
        z = abs(now)
        if z == 0:
            break

    if now < 0:
        start += 1
    else:
        end -= 1
print(ans[0], ans[1])
