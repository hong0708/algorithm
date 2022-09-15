import copy


def make(start_x, start_y, start_left):
    global answer
    global ans
    x = start_x
    y = start_y
    add(x, y)
    can = True
    while can:
        for a in range(len(start_left)):
            if y == start_left[a][0]:
                x = start_left[a][0]
                y = start_left[a][1]
                add(x, y)
                can = True
                break
            can = False
    if len(answer) > len(ans):
        ans = answer
        answer = []
    else:
        answer = []


def add(start, end):
    global answer
    answer.append(start)
    answer.append(end)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = list(map(int, input().split()))
    arr = []
    answer = []
    ans = []
    for i in range(0, 2 * n, 2):
        arr.append([data[i], data[i + 1]])
    for i in range(n):
        left = arr.copy()
        left.pop(i)
        make(arr[i][0], arr[i][1], left)
    print("#{}".format(tc))
    for z in ans:
        print(z, end=" ")
    print()
