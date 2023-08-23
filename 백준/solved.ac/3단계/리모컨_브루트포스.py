#

n = int(input())
ans = abs(n - 100)
m = int(input())
if m:
    arr = list(map(int, input().split()))
else:
    arr = []

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in arr:
            break
        elif j == len(i) - 1:
            ans = min(ans, abs(int(i) - n) + len(i))

print(ans)
