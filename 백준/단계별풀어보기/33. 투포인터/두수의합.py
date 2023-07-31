# https://www.acmicpc.net/submit/3273

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
start, end, ans = 0, n - 1, 0
while start != end:
    now = arr[start] + arr[end]
    if now > x:
        end -= 1
    elif now == x:
        ans += 1
        start += 1
    else:
        start += 1
print(ans)
