tc = int(input())
for t in range(tc):
    n = int(input())
    answer = 0
    arr = list(map(int, input().split()))

    maxDay = arr[-1]
    dayCount = 0
    buyCount = 0

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= maxDay:
            answer += dayCount * maxDay
            maxDay = arr[i]
            dayCount = 0
        elif arr[i] < maxDay:
            dayCount += 1
            buyCount += arr[i]

        if i == 0:
            answer += dayCount * maxDay

    answer -= buyCount
    print("#{} {}".format(t + 1, answer))
