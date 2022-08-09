t = int(input())
for a in range(t):
    answer = 0
    length, order = map(str, input().split())
    data = [list(map(int, input().split())) for _ in range(int(length))]
    length = int(length)

    if order == 'up':
        for i in range(length):
            nowList = []
            for j in range(length):
                nowList.append(data[j][i])

            whatNumber = []
            result = []
            for k in range(len(nowList)):
                if nowList[k] != 0:
                    if len(whatNumber) != 0 and whatNumber[-1] == nowList[k]:
                        result.append(nowList[k] * 2)
                        whatNumber.pop(-1)

                    elif len(whatNumber) != 0 and whatNumber[-1] != nowList[k]:
                        result.append(whatNumber[-1])
                        whatNumber.pop(-1)
                        whatNumber.append(nowList[k])

                    elif len(whatNumber) == 0:
                        whatNumber.append(nowList[k])
            if len(whatNumber) != 0:
                result.append(whatNumber[-1])

            plusZ = len(nowList) - len(result)
            for _ in range(plusZ):
                result.append(0)

            for z in range(length):
                data[z][i] = result[z]

    elif order == 'down':
        for i in range(length):
            nowList = []
            for j in range(length - 1, -1, -1):
                nowList.append(data[j][i])

            whatNumber = []
            result = []
            for k in range(len(nowList)):
                if nowList[k] != 0:
                    if len(whatNumber) != 0 and whatNumber[-1] == nowList[k]:
                        result.append(nowList[k] * 2)
                        whatNumber.pop(-1)

                    elif len(whatNumber) != 0 and whatNumber[-1] != nowList[k]:
                        result.append(whatNumber[-1])
                        whatNumber.pop(-1)
                        whatNumber.append(nowList[k])

                    elif len(whatNumber) == 0:
                        whatNumber.append(nowList[k])
            if len(whatNumber) != 0:
                result.append(whatNumber[-1])

            plusZ = len(nowList) - len(result)
            for _ in range(plusZ):
                result.append(0)

            for z in range(length):
                data[length - z - 1][i] = result[z]

    elif order == 'left':
        for i in range(length):
            nowList = []
            for j in range(length):
                nowList.append(data[i][j])

            whatNumber = []
            result = []
            for k in range(len(nowList)):
                if nowList[k] != 0:
                    if len(whatNumber) != 0 and whatNumber[-1] == nowList[k]:
                        result.append(nowList[k] * 2)
                        whatNumber.pop(-1)

                    elif len(whatNumber) != 0 and whatNumber[-1] != nowList[k]:
                        result.append(whatNumber[-1])
                        whatNumber.pop(-1)
                        whatNumber.append(nowList[k])

                    elif len(whatNumber) == 0:
                        whatNumber.append(nowList[k])
            if len(whatNumber) != 0:
                result.append(whatNumber[-1])

            plusZ = len(nowList) - len(result)
            for _ in range(plusZ):
                result.append(0)

            for z in range(length):
                data[i][z] = result[z]

    elif order == 'right':
        for i in range(length):
            nowList = []
            for j in range(length - 1, -1, -1):
                nowList.append(data[i][j])

            whatNumber = []
            result = []
            for k in range(len(nowList)):
                if nowList[k] != 0:
                    if len(whatNumber) != 0 and whatNumber[-1] == nowList[k]:
                        result.append(nowList[k] * 2)
                        whatNumber.pop(-1)

                    elif len(whatNumber) != 0 and whatNumber[-1] != nowList[k]:
                        result.append(whatNumber[-1])
                        whatNumber.pop(-1)
                        whatNumber.append(nowList[k])

                    elif len(whatNumber) == 0:
                        whatNumber.append(nowList[k])
            if len(whatNumber) != 0:
                result.append(whatNumber[-1])

            plusZ = len(nowList) - len(result)
            for _ in range(plusZ):
                result.append(0)

            for z in range(length):
                data[i][length - z - 1] = result[z]

    print("#{}".format(a + 1))
    for w in data:
        for h in w:
            print(h, end=' ')
        print()