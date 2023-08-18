# https://www.acmicpc.net/problem/11444
import sys

n = int(sys.stdin.readline())
m = [[1, 1], [1, 0]]


def m_matrix(arr1, arr2):
    ans = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += arr1[i][k] * arr2[k][j] % 1000000007
    return ans


def di(arr_x, y):
    if y == 1:
        return arr_x
    else:
        temp = di(arr_x, y // 2)
        if y % 2 == 0:
            return m_matrix(temp, temp)
        else:
            return m_matrix(m_matrix(temp, temp), arr_x)


result = di(m, n)

# Fn 출력
print(result[0][1] % 1000000007)
