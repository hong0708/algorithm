n = int(input())

r = list(map(int, input().split()))
v = list(map(int, input().split()))
min_ans = 0

i = 0
while i < len(v) - 1:
    loc = 1
    pay = 0
    while i + loc < len(v):
        if v[i] > v[i + loc]:
            for j in range(i, i + loc):
                pay += (r[j] * v[i])
            i += loc
            break
        elif i + loc == len(v) - 1:
            for j in range(i, i + loc):
                pay += (r[j] * v[i])
            i += loc
            break
        else:
            loc += 1
    min_ans += pay
print(min_ans)
