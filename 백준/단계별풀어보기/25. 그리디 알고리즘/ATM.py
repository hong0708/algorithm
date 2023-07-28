n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = arr[0]
b = arr[0]
for i in range(1, n):
    ans += (b + arr[i])
    b += arr[i]
print(ans)
