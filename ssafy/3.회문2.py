for t in range(10):
    tc = int(input())
    lenOfData = 100
    answer = 0
    data = [list(map(str, input())) for _ in range(100)]
    find = False

    for answer in range(100, 1, -1):
        for i in range(100):
            for j in range(101 - answer):
                letter = []
                reversLetter = []
                for k in range(answer):
                    letter.append(data[i][j + k])
                reversLetter = letter[::-1]
                if letter == reversLetter:
                    find = True
                    break
        if find:
            break

        for x in range(100):
            for y in range(101 - answer):
                letter = []
                reversLetter = []
                for z in range(answer):
                    letter.append(data[y + z][x])
                reversLetter = letter[::-1]
                if letter == reversLetter:
                    find = True
                    break
        if find:
            break

    print("#{} {}".format(t + 1, answer))
