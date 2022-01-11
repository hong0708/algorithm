n, k, q, m = map(int, input().split())
student = [False] * (n + 3)
sleep = list(map(int, input().split()))
code = list(map(int, input().split()))
answer = 0
for i in code:
    if i in sleep:
        continue
    else:
        for j in range(i, len(student), i):
            if j in sleep:
                continue
            else:
                student[j] = True
for _ in range(m):
    first, second = map(int, input().split())
    if second < len(student):
        a = student[first:second+1]
    else:
        a = student[first:second]
    answer += a.count(False)
print(answer)
