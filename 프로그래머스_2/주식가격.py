prices = [1, 2, 3, 2, 3]
answer = []
for i in range(len(prices)-1):
    count = 0
    for j in range(i + 1, len(prices)):
        count += 1
        if prices[i] > prices[j]:
            break
    answer.append(count)

answer.append(0)
print answer
