import itertools

data = []
for _ in range(9):
    data.append(int(input()))

for i in itertools.combinations(data, 7):
    if sum(i) == 100:
        answer = i
        break
answer = sorted(answer)
for j in answer:
    print(j)