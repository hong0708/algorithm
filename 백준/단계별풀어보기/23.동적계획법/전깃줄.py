# https://www.acmicpc.net/problem/2565
# 시작점을 기준으로 정렬을 하고 뒤 숫자를 비교해 이전 숫자보다 큰지 비교함
n = int(input())
arr = []
ans = [1 for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

for a in range(1, n):
    for b in range(0, a):
        if arr[b][1] < arr[a][1]:
            ans[a] = max(ans[a], ans[b] + 1)

print(n - max(ans))
