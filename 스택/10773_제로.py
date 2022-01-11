#https://www.acmicpc.net/problem/10773
num = int(input())
answer = []
for _ in range(num):
    a = int(input())
    if a != 0:
        answer.append(a)
    else:
        answer.pop()
add = sum(answer)
print(add)