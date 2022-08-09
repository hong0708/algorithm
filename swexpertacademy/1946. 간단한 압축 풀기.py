tc = int(input())
for t in range(tc):
    testNum = int(input())

    printArr = ""
    print("#{}".format(t + 1))
    for _ in range(testNum):
        char, count = input().split()
        count = int(count)

        printArr += char * count

    for i in range(0, len(printArr)+1, 10):
        print(printArr[i: i + 10])
