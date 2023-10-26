# https://www.acmicpc.net/problem/2193

n = int(input())
arr = [[0, 0] for _ in range(n + 1)]
arr[1] = [0, 1]
for i in range(2, n + 1):
    arr[i][0] = arr[i - 1][0] + arr[i - 1][1]
    arr[i][1] = arr[i - 1][0]
print(sum(arr[n]))
