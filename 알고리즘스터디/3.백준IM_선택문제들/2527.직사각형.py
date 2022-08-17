for _ in range(4):
    data = list(map(int, input().split()))
    sq1 = []
    sq2 = []

    sq1.append(data[:4])
    sq2.append(data[4:])

    #print(sq1, sq2)

    sq1Code = []
    sq2Code = []
    for i in range(data[0], data[2] + 1):
        for j in range(data[1], data[3] + 1):
            sq1Code.append([i, j])

    for i in range(data[4], data[6] + 1):
        for j in range(data[5], data[7] + 1):
            sq2Code.append([i, j])

    common = []
    for a in range(len(sq1Code)):
        if sq1Code[a] in sq2Code:
            common.append(sq1Code[a])

    if len(common) == 1:
        print('c')
    elif len(common) == 0:
        print('d')
    else:
        print('a,b')
