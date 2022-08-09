tc = int(input())

for t in range(tc):
    countDay = int(input())
    startDay = countDay
    data = list(map(int, input().split()))

    answer = 0
    i = 0
    while True:
        if startDay != countDay:
            answer += 1

        if data[i] == 1:
            countDay -= 1

        if countDay == 0:
            break
        if i == 6:
            i = 0
        else:
            i += 1
    print("#{} {}".format(t + 1, answer + 1))
