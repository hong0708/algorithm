people = list(map(int, input().split()))
timeset = [False] * (people[1] + 1)
answer = 0
for i in range(people[0]):
    a = int(input())
    for j in range(a, people[1] + 1, a):
        if not timeset[j]:
            timeset[j] = True
            answer += 1
print(answer)
