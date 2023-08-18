# https://www.acmicpc.net/problem/1629
import sys

a, b, c = map(int, sys.stdin.readline().split())


def cal(x, y):
    if y == 1:
        return x % c
    else:
        if y % 2 == 0:
            return cal(x, y // 2) ** 2 % c
        else:
            return cal(x, y // 2) ** 2 * cal(x, 1) % c


print(cal(a, b))
