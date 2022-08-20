n = int(input())
for i in range(n):
    dataA = list(map(int, input().split()))[1:]
    dataB = list(map(int, input().split()))[1:]
    countA = [dataA.count(4), dataA.count(3), dataA.count(2), dataA.count(1)]
    countB = [dataB.count(4), dataB.count(3), dataB.count(2), dataB.count(1)]

    if countA[0] > countB[0]:
        print('A')
    elif countA[0] < countB[0]:
        print('B')
    elif countA[1] > countB[1]:
        print('A')
    elif countB[1] > countA[1]:
        print('B')
    elif countA[2] > countB[2]:
        print('A')
    elif countB[2] > countA[2]:
        print('B')
    elif countA[3] > countB[3]:
        print('A')
    elif countB[3] > countA[3]:
        print('B')
    else:
        print('D')
