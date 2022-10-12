from itertools import combinations_with_replacement

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    data = []
    count = 1000000

    for _ in range(n):
        temp = list(input())
        data.append(temp)

    case = []
    for a in range(n - 2):
        case.append(a + 1)

    for line in combinations_with_replacement(case, 2):
        line = list(line)
        tempCount = 0

        if line[0] == line[1]:
            for a in range(0, line[0]):
                for b in range(0, m):
                    if data[a][b] != 'W':
                        tempCount += 1

            for b in range(0, m):
                if data[line[0]][b] != 'B':
                    tempCount += 1

            for a in range(line[0] + 1, n):
                for b in range(0, m):
                    if data[a][b] != 'R':
                        tempCount += 1
        else:
            for a in range(0, line[0]):
                for b in range(0, m):
                    if data[a][b] != 'W':
                        tempCount += 1

            for a in range(line[0], line[1] + 1):
                for b in range(0, m):
                    if data[a][b] != 'B':
                        tempCount += 1

            for a in range(line[1] + 1, n):
                for b in range(0, m):
                    if data[a][b] != 'R':
                        tempCount += 1
        count = min(tempCount, count)
    print("#{} {}".format(t, count))
