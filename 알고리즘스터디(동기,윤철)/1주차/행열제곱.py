# https://www.acmicpc.net/problem/10830
import sys

n, b = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def cal(arr1, arr2):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += arr1[i][k] * arr2[k][j] % 1000
    return ans


def di(arr_x, y):
    if y == 1:
        return arr_x
    else:
        temp = di(arr_x, y // 2)
        if y % 2 == 0:
            return cal(temp, temp)
        else:
            return cal(cal(temp, temp), arr_x)


result = di(arr, b)
for i in range(n):
    for j in range(n):
        result[i][j] %= 1000
for i in range(n):
    print(*result[i])

# for row in result:
#    for col in row:
#        print(col % 1000, end=" ")
#    print()
