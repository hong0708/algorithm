m = int(input())
n = int(input())

answer = []
arr = [False, False] + [True for _ in range(10000)]
for i in range(2, n):
    for j in range(2 * i, n + 1, i):
        arr[j] = False

for a in range(m, n + 1):
    if arr[a]:
        answer.append(a)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])
