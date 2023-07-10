t = int(input())
for i in range(t):
    d = 2
    answer = 1
    a, b = map(int, input().split())
    while d <= min(a, b):
        if a % d == 0 and b % d == 0:
            answer *= d
            a //= d
            b //= d
        else:
            d += 1
    print(answer * a * b)