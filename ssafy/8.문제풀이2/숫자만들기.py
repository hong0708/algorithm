operatorList = ['+', '-', '*', '/']


def calculation(x, y, oper):
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '*':
        return x * y
    else:
        return int(x / y)


def step(idx, beforeNum):
    global maxAns
    global minAns

    if idx == n - 1:
        if beforeNum > maxAns:
            maxAns = beforeNum
        if beforeNum < minAns:
            minAns = beforeNum
        return
    for i in range(4):
        if operatorCount[i]:
            operatorCount[i] -= 1
            step(idx + 1, calculation(beforeNum, data[idx + 1], operatorList[i]))
            operatorCount[i] += 1


t = int(input())
for tc in range(t):
    n = int(input())

    operatorCount = list(map(int, input().split()))
    data = list(map(int, input().split()))

    minAns = 100000000
    maxAns = -100000000
    step(0, data[0])
    print("#{} {}".format(tc + 1, maxAns - minAns))
