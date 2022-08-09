from itertools import combinations

tc = int(input())

for t in range(tc):
    data = list(map(str, input()))
    target = [i for i in range(len(data))]

    minNum, maxNum = int(''.join(data)), int(''.join(data))

    for value in combinations(target, 2):
        i, j = value
        data[i], data[j] = data[j], data[i]
        if data[0] == '0':
            data[i], data[j] = data[j], data[i]
            continue
        if int(''.join(data)) < minNum:
            minNum = int(''.join(data))
        if int(''.join(data)) > maxNum:
            maxNum = int(''.join(data))
        data[i], data[j] = data[j], data[i]

    print("#{} {} {}".format(t + 1, minNum, maxNum))
