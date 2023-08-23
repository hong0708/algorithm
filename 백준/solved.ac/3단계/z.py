# https://www.acmicpc.net/problem/1074

n, r, c = map(int, input().split())
ans = 0

while n > 0:
    now = 2 ** (n - 1)

    # 1사분면
    if r < now and c < now:
        ans += 0
    # 2사분면
    elif r < now and c >= now:
        ans += 2 ** ((n-1) * 2) * 1
        c -= now
    # 3사분면
    elif r >= now and c < now:
        ans += 2 ** ((n-1) * 2) * 2
        r -= now
    # 4사분면
    else:
        ans += 2 ** ((n-1) * 2) * 3
        c -= now
        r -= now
    n -= 1
print(ans)
