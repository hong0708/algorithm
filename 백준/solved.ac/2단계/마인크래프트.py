# https://www.acmicpc.net/problem/18111

n, m, b = map(int, input().split())
arr = []

ground = 0

l = 0
s = 256

time = 0
ans = [-1, -1]

for _ in range(n):
    impl = list(map(int, input().split()))
    l = max(l, max(impl))
    s = min(s, min(impl))
    arr.append(impl)

ground = s
while s <= ground <= l:
    bag = b
    time = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] < ground:
                bag -= ground - arr[i][j]
                time += ground - arr[i][j]

            elif arr[i][j] > ground:
                bag += arr[i][j] - ground
                time += 2 * (arr[i][j] - ground)

    if bag >= 0:
        if ans[0] == -1:
            ans[0] = time
            ans[1] = ground
        else:
            if time <= ans[0]:
                ans[0] = time
                ans[1] = ground
    else:
        break
    ground += 1

print(*ans)
