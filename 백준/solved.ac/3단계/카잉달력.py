# https://www.acmicpc.net/problem/6064

from math import lcm

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    l = lcm(m, n)
    ans = -1

    now = 0
    while m * now <= l:
        if n != y:
            if m * now + x == y + ((m * now + x) // n * n):
                ans = m * now + x
                break
        else:
            if m * now + x == ((m * now + x) // n * n):
                ans = m * now + x
                break
        now += 1
    print(ans)
