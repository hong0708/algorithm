def makeList(num):
    numArr = []
    for _ in range(10):
        numArr.append(num % 10)
        num //= 10
        if num == 0:
            # numArr.sort()
            return numArr
    return numArr


tc = int(input())
for t in range(tc):
    arr = int(input())
    orgNum = arr
    numberArr = makeList(arr)

    answer = 'impossible'

    multiCount = 2
    while multiCount < 10:
        orgNumArr = numberArr
        afterNum = makeList(orgNum * multiCount)
        if len(afterNum) != len(orgNumArr):
            multiCount += 1
            break
        else:
            for i in range(len(orgNumArr)):
                if orgNumArr[i] not in afterNum:
                    break
                if i == len(afterNum) - 1 and orgNumArr[i] in afterNum:
                    answer = 'possible'
                    multiCount = 10
            multiCount += 1

    print("#{} {}".format(t + 1, answer))
