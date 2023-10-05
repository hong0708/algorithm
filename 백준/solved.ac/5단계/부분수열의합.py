# https://www.acmicpc.net/problem/1182

from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    for j in combinations(arr, i):
        j = list(j)
        if sum(j) == s:
            ans += 1
print(ans)
