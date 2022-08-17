for _ in range(4):
    data = list(map(int, input().split()))
    x1, x2, x3, x4 = data[:4]
    y1, y2, y3, y4 = data[4:]

    if (x1 == y3 and x2 == y4) or (y1 == x3 and y2 == x4) or (x3 == y1 and x2 == y4) or (x1 == y3 and x4 == y2):
        print('c')
    elif (x3 < y1) or (x4 < y2) or (x2 > y4) or (x1 > y3):
        print('d')
    elif (x4 == y2) or (x2 == y4) or (x3 == y1) or (x1 == y3):
        print('b')
    else:
        print('a')
