n, m = map(int, input().split())

arr = []
impl = [[0] * (n + 1) for i in range(n + 1)]

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

for j in range(1, n + 1):
    for k in range(1, n + 1):
        impl[j][k] = impl[j][k - 1] + impl[j - 1][k] - impl[j - 1][k - 1] + arr[j - 1][k - 1]

for z in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = impl[x2][y2] - impl[x2][y1 - 1] - impl[x1 - 1][y2] + impl[x1 - 1][y1 - 1]
    print(result)
