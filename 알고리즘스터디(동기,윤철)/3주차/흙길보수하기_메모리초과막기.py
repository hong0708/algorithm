# https://www.acmicpc.net/problem/1911

n, l = map(int, input().split())

arr = []

for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])
ans = 0
arr.sort(key=lambda x: x[0])
impl = -1

for i in arr:
    s, e = i[0], i[1]

    if impl >= s:
        s = impl + 1

    if (e - s) % l == 0:
        ans += (e - s) // l
        impl = s + (e - s) // l * l - 1
    else:
        ans += (e - s) // l + 1
        impl = s + (e - s) // l * l - 1 + l

print(ans)
