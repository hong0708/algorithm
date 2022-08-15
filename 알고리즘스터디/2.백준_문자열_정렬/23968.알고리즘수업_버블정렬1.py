length, k = map(int, input().split())
data = list(map(int, input().split()))

count = 0
answer = [-1]

for j in range(length - 1, 0, -1):
    for i in range(j):
        if data[i] > data[i + 1]:
            temp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = temp
            count += 1

            if count == k:
                answer[0] = data[i]
                answer.append(data[i + 1])
                break

for j in answer:
    print(j, end=" ")
