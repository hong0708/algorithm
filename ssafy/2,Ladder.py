def checkX(x, y):
    x += 1
    while True:
        if x == 99 and data[x][y] == 2:
            isTwo = True
            break
        if x == 99 and data[x][y] == 1:
            isTwo = False
            break

        if y + 1 < 100 and data[x][y + 1] == 1:
            y += 1
            x += 1
        if y - 1 > 0 and data[x][y - 1] == 1:
            y -= 1
            x += 1
        else:
            x += 1
    return isTwo


for t in range(10):
    testNum = int(input())
    #data = []
    answer = 0
    route = False
    data = [list(map(int, input().split())) for _ in range(100)]

    #for _ in range(100):
    #   data.append(list(map(int, input().split())))
    
    for i in range(100):
        if data[0][i] == 1:
            route = checkX(0, i)
        if route:
            answer = i

    print("#{} {}".format(t + 1, answer))
