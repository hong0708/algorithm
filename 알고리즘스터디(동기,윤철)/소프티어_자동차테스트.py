n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(q):
    x = int(input())
    start = 0
    end = n - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            ans = mid * (n - 1 - mid)
            break
        elif arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
    if ans == -1:
        print(0)
    else:
        print(ans)
