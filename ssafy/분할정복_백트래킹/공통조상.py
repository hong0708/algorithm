from collections import deque


def findParent(x, parents, who):
    global left
    global right
    now_parents = parents

    if x == 1:
        if who == "left":
            left = parents
            return
        else:
            right = parents
            return
    for i in range(len(index_data)):
        if int(x) in index_data[i]:
            now_parents.append(i)
            findParent(i, now_parents, who)
            break


def findSize(x):
    global size
    sizeList = [x]
    toGo = deque()
    toGo.append(x)
    while toGo:
        now = toGo.pop()
        for j in range(1, len(index_data[now])):
            sizeList.append(index_data[now][j])
            toGo.append(index_data[now][j])
    size = len(sizeList)

t = int(input())
for tc in range(1, t + 1):
    answer = 0
    size = 0
    v, e, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    index_data = list([0] for _ in range(v + 1))

    for i in range(0, len(arr) - 1, 2):
        index_data[arr[i]].append(arr[i + 1])

    left = []
    findParent(a, left, "left")
    right = []
    findParent(b, right, "right")

    for p in right:
        if p in left:
            answer = p
            break

    findSize(p)
    print("#{} {} {}".format(tc, answer, size))
