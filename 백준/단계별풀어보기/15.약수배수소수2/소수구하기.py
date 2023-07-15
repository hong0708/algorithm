m, n = map(int, input().split())
arr = [True, True] + [False for _ in range(n)]
for i in range(2, int(len(arr) ** 0.5) + 1):
    if not arr[i]:
        for j in range(2 * i, n + 1, i):
            arr[j] = True
for a in range(m, n + 1):
    if not arr[a]:
        print(a)
