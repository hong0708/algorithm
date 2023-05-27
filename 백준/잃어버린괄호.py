impl = list(input().split("-"))

answer = 0
for i in range(len(impl)):
    c = impl[i]
    cal = list(map(int, c.split("+")))
    num = 0
    if i == 0:
        answer += sum(cal)
    else:
        answer -= sum(cal)
print(answer)