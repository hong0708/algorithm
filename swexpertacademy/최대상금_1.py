import itertools
from collections import deque
import copy


def changeNum(data, swc):
    global changeNumberList
    numbers = deque()
    numbers.append([data, swc])
    # numbers.append(swc)

    while numbers:
        a = numbers.popleft()
        base = a[0]
        swCount = a[1]
        # base = numbers.popleft()
        # swCount = numbers.popleft()

        caseList = []
        for i in range(len(base)):
            caseList.append(i)

        for case in itertools.combinations(caseList, 2):
            case = list(case)
            ch_base = copy.deepcopy(base)
            num1 = base[case[0]]
            num2 = base[case[1]]
            ch_base[case[0]] = num2
            ch_base[case[1]] = num1

            if swCount > 1:
                temp = int(''.join(map(str, ch_base)))
                if visited.get(temp) != swCount - 1:
                    visited[temp] = swCount - 1
                    numbers.append([ch_base, swCount - 1])
            else:
                if ch_base not in changeNumberList:
                    changeNumberList.append(ch_base)


def makeNum(numList):
    size = 10 ** (len(numList) - 1)
    number = 0

    loc = 0
    while loc != len(numList):
        number += size * numList[loc]
        size //= 10
        loc += 1
    return number


t = int(input())
for tc in range(1, t + 1):
    num, sw = map(int, input().split())
    arr = []
    answer = 0
    visited = {}
    while True:
        arr.append(num % 10)
        if num // 10 < 1:
            break
        num //= 10
    arr.reverse()
    caseList = []
    for i in range(len(arr)):
        caseList.append(i)

    changeNumberList = []
    changeNum(arr, sw)

    for a in changeNumberList:
        temp = makeNum(a)
        if answer < temp:
            answer = temp
    print("#{} {}".format(tc, answer))
