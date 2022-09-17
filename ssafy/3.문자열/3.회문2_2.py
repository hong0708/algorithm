for t in range(10):
    tc = int(input())
    answer = 0
    data = [list(map(str, input())) for _ in range(100)]

    for answer in range(1, 101):
        find = False
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
        if not find:
            answer -= 1
            break

    print("#{} {}".format(t + 1, answer))
