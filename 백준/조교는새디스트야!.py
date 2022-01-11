count = int(input())
answer = 0

j = 1

student = list(map(int,input().split()))
for i in range(count):
    if student[i] == j:
        answer += 1
    j += 1
print(count - answer)