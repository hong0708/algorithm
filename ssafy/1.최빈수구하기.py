tc = int(input())

for t in range(tc):
    testCount = int(input())
    data = list(map(int, input().split()))
    countArr = [0] * 101

    for i in range(len(data)):
        countArr[data[i]] += 1

    answer = 0
    maxCount = 0
    for i in range(len(countArr)):
        if maxCount <= countArr[i]:
            maxCount = countArr[i]
            answer = i

    print("#{} {}".format(t + 1, answer))
