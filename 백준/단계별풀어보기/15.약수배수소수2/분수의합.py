a, b = map(int, input().split())
c, d = map(int, input().split())
x = a * d + c * b
y = b * d

d = 2
while d <= min(x, y):
    if x % d == 0 and y % d == 0:
        x //= d
        y //= d
    else:
        d += 1
print(x, y)
