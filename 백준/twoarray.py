n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min = min(n, m)
answer = []
for i in range(min):
    if a[i] < b[i]:
        answer.append(a[i])
        answer.append(b[i])
    else:
        answer.append(b[i])
        answer.append(a[i])
if min == n:
    answer.append(b[n:])
else:
    answer.append(a[m:])
print(answer)