n = int(input())
data = list(map(int, input().split()))
students = int(input())
for i in range(students):
    switchNum = list(map(int, input().split()))
    if switchNum[0] == 1:
        for a in range(switchNum[1] - 1, n, switchNum[1]):
            if data[a] == 1:
                data[a] = 0
            else:
                data[a] = 1
    else:
        switchNum[1] -= 1
        if data[switchNum[1]] == 1:
            data[switchNum[1]] = 0
        else:
            data[switchNum[1]] = 1
        b = 0
        while True:
            b += 1
            if switchNum[1] - b > -1 and switchNum[1] + b < n and data[switchNum[1] + b] == data[switchNum[1] - b]:
                if data[switchNum[1] + b]:
                    data[switchNum[1] + b] = 0
                    data[switchNum[1] - b] = 0
                else:
                    data[switchNum[1] + b] = 1
                    data[switchNum[1] - b] = 1
            else:
                break
for z in range(1, n + 1):
    print(data[z - 1], end=" ")
    if z % 20 == 0:
        print()
