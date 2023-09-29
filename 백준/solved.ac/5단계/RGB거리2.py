# https://www.acmicpc.net/problem/17404
# 해당 순서에 각각의 색에서 기존의 값중 작은 경우의 색을 더해가며 다음 경우를 본다

from copy import deepcopy

n = int(input())
arr = []
INF = 1e9
ans = INF

for _ in range(n):
    arr.append(list(map(int, input().split())))

for x in range(3):
    impl = deepcopy(arr)
    for i in range(3):
        if i == x:
            impl[1][x] = INF
        else:
            impl[1][i] += impl[0][x]
    if n >= 3:
        for i in range(2, n):
            impl[i][0] += min(impl[i - 1][1], impl[i - 1][2])
            impl[i][1] += min(impl[i - 1][0], impl[i - 1][2])
            impl[i][2] += min(impl[i - 1][0], impl[i - 1][1])
        impl[n - 1][x] = INF
        ans = min(min(impl[n - 1]), ans)

print(ans)
