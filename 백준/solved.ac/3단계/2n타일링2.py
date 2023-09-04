# https://www.acmicpc.net/problem/11727

n = int(input())
arr = [0 for _ in range(n + 2)]

arr[1] = 1
arr[2] = 3

for i in range(n + 1):
    if not arr[i]:
        arr[i] = (arr[i - 2] * 2 + arr[i - 1]) % 10007
print(arr[n])
