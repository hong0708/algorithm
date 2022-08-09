tc = int(input())

for t in range(tc):
    countDay = int(input())
    countClass = countDay
    data = list(map(int, input().split()))

    oneWeek = sum(data)

    if countDay % oneWeek == 0:
        answer = (countDay // oneWeek - 1) * 7
        countClass -= oneWeek * (countDay // oneWeek - 1)
    else:
        answer = (countDay // oneWeek) * 7
        countClass -= oneWeek * (countDay // oneWeek)

    for i in range(7):
        answer += 1
        if data[i] == 1:
            countClass -= 1
        if countClass == 0:
            break

    firstClass = 0
    for i in range(7):
        if data[i] == 1:
            firstClass = i
    answer -= firstClass

    print("#{} {}".format(t + 1, answer))
