w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

count = 0
dp = 1
dq = 1

while True:
    if count == t:
        print(p, q)
        break
    if -1 < p + dp < w + 1 and -1 < q + dq < h + 1:
        p += dp
        q += dq
        count += 1
    else:
        if p == w:
            if q == h:
                dp = -1
                dq = -1
            elif q == 0:
                dp = -1
                dq = 1
            else:
                dp *= -1
                dq *= 1

        elif p == 0:
            if q == h:
                dp = 1
                dq = -1
            elif q == 0:
                dp = 1
                dq = 1
            else:
                dp *= -1
                dq *= 1

        elif q == h:
            dp *= 1
            dq *= -1

        elif q == 0:
            dp *= 1
            dq *= -1
