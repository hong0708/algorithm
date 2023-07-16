def f(a):
    ans = 1
    for j in range(1, a + 1):
        ans *= j
    return ans


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(f(m) // (f(n) * f(m - n)))
