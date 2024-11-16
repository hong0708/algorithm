t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    ans = 0
    a, b = 0, 0
    loc = 0
    for i in range(x):
        while b < y and A[i] > B[b]:
            b += 1
            loc += 1
        else:
            ans += loc
    print(ans)