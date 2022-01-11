# https://www.acmicpc.net/problem/1904
num = int(input())

a = 1
b = 2
for _ in range(num - 2):
    c = a + b
    a, b = b % 15746, c % 15746

print(c)
