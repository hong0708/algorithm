n = int(input())
numList = []
for i in range(1, n + 1):
    numList.append(i)
print(numList)
while len(numList) != 1:
    count = len(numList)
    a = 0
    for i in range(0, count):
        if i % 2 == 0:
            del numList[a]
        else: a += 1
        print(numList)
    print(numList)
print(numList[0])
