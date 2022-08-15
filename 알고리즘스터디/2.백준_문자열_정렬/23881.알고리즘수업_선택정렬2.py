length, k = map(int, input().split())
data = list(map(int, input().split()))

count = 0

for j in range(length, 1, -1):
    maxNum = max(data[:j])
    maxNumIdx = data.index(maxNum)
    if data[j - 1] != maxNum:
        temp = data[j - 1]
        data[j - 1] = maxNum
        data[maxNumIdx] = temp
        count += 1
    if count == k:
        break

if count != k:
    print(-1)
else:
    for i in data:
        print(i, end=" ")
