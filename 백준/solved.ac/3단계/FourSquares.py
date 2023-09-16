# https://www.acmicpc.net/problem/17626

n = int(input())
arr = [0, 1] + [0 for _ in range(n - 1)]

loc = 1
while loc <= n:
    if arr[loc] != 1:
        now = 1
        while now ** 2 < loc:
            if loc - now ** 2 > 0:
                if arr[loc] == 0:
                    arr[loc] = arr[loc - now ** 2] + 1
                else:
                    arr[loc] = min(arr[loc - now ** 2] + 1, arr[loc])
                if arr[loc] == 2:
                    break
            now += 1
    if loc ** 2 <= n:
        arr[loc ** 2] = 1
    loc += 1
print(arr[n])
