n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
answer = [0 for _ in range(n + 1)]
max_num = 0

for i in range(n):
    max_num = max(max_num, answer[i])
    if data[i][0] + i > n:
        continue

    answer[data[i][0] + i] = max(answer[data[i][0] + i], max_num + data[i][1])

print(max(answer))
