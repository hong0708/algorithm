# https://www.acmicpc.net/problem/9251

a = input()
b = input()
la = len(a)
lb = len(b)

arr = [[0] * (lb + 1) for _ in range(la + 1)]

for i in range(1, la + 1):
    for j in range(1, lb + 1):
        if a[i - 1] == b[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
print(arr[la][lb])
