for _ in range(4):
    data = list(map(int, input().split()))

    if data[0] <= data[4]:
        sq1 = data[:4]
        sq2 = data[4:]
    else:
        sq2 = data[:4]
        sq1 = data[4:]

    if sq1[2] < sq2[0]:
        print('d')
    elif sq1[3] < sq2[1]:
        print('d')
    elif sq1[1] > sq2[3]:
        print('d')
    else:
        if sq1[2] == sq2[0] and sq1[3] == sq2[1]:
            print('c')
        elif sq1[2] == sq2[0] and sq1[1] == sq2[3]:
            print('c')
        else:
            if sq1[2] == sq2[0]:
                if sq2[3] > sq1[1] > sq2[1]:
                    print('b')
                elif sq1[3] > sq2[1] > sq1[1]:
                    print('b')
            elif sq1[3] == sq2[1] and sq1[2] > sq2[0]:
                print('b')
            elif sq1[1] == sq2[3] and sq1[2] > sq2[0]:
                print('b')
            else:
                print('a')
