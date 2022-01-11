# https://www.acmicpc.net/problem/1406
#
numList = list(raw_input())
n = int(input())
point = len(numList)
while n:
    command = list(raw_input())
    if command[0] == 'P':
        numList.insert(point, command[2])
    elif command[0] == 'L':
        point -= 1
        if point < 0:
            point += 1
    elif command[0] == 'D':
        point += 1
        if point < len(numList):
            point -= 1
    elif command[0] == 'B':
        if point != 0:
            del numList[point - 1]
            point -= 1
    n -= 1
print(numList)
