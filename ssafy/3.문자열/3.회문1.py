for t in range(10):
    lenOfData = int(input())
    answer = 0
    data = [list(map(str, input())) for _ in range(8)]

    for i in range(8):
        for j in range(9 - lenOfData):
            letter = []
            reversLetter = []
            for k in range(lenOfData):
                letter.append(data[i][j + k])
            reversLetter = letter[::-1]
            if letter == reversLetter:
                answer += 1

    for x in range(8):
        for y in range(9 - lenOfData):
            letter = []
            reversLetter = []
            for z in range(lenOfData):
                letter.append(data[y + z][x])
            reversLetter = letter[::-1]
            if letter == reversLetter:
                answer += 1

    print("#{} {}".format(t + 1, answer))
