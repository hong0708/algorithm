# https://www.acmicpc.net/problem/2609

x, y = map(int, input().split())


def gcd(a, b):
    while (b > 0):
        tmp = a
        a = b
        b = tmp % b
    return a


ans1 = gcd(x, y)
ans2 = x * y // ans1

print(ans1)
print(ans2)