# https://www.acmicpc.net/problem/1149
# 해당 순서에 각각의 색에서 기존의 값중 작은 경우의 색을 더해가며 다음 경우를 본다
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])
print(min(arr[n - 1]))
