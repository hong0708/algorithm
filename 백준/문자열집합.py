n, m = map(int, input().split())
s = []
ans = 0
for i in range(n):
    s.append(input())
s = set(s)
for j in range(m):
    txt = input()
    if txt in s:
        ans += 1

print(ans)
