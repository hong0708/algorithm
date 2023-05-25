def reverse(a):
    b = 0
    d = 10
    D = 100
    while a != 0:
        b += (a % 10) * D
        a /= d
        D /= d
    return b


a, b = map(int, input().split())

d = 10
while True:
    if a % d > b % d:
        answer = a
        break
    elif a % d < b % d:
        answer = b
        break
    else:
        d *= 10
