# https://www.acmicpc.net/problem/15664

num = list(map(int, input().split()))

ans = 0

for i in num:
    ans += i ** 2

print(ans % 10)
