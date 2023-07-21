# https://www.acmicpc.net/status?user_id=gaogai2&problem_id=11054&from_mine=1
# 가장 긴 수열을 찾는 과정을 앞에서 뒤에서 한뒤 합
n = int(input())
arr1 = list(map(int, input().split()))
ans1 = [1 for _ in range(n)]

arr2 = []
ans2 = [0 for _ in range(n)]
for a in range(n):
    arr2 = [arr1[a]] + arr2

for i in range(n):
    for j in range(i):
        if arr1[i] > arr1[j]:
            ans1[i] = max(ans1[i], ans1[j] + 1)

for i in range(n):
    for j in range(i):
        if arr2[i] > arr2[j]:
            ans2[i] = max(ans2[i], ans2[j] + 1)

ans = []
for b in range(n):
    ans.append(ans1[b] + ans2[n-b-1])
print(max(ans))
