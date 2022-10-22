n = int(input())
data = list(map(int, input().split()))
answer = [1 for _ in range(n)]

for i in range(0, n):
    for j in range(i):
        if data[j] > data[i]:
            answer[i] = max(answer[i], answer[j] + 1)

print(max(answer))
