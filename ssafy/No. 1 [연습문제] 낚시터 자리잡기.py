from collections import deque
import itertools
import copy


def checkRoute(data):
    global mincount

    people = data
    fishing = [1] + [0] * n
    route = deque()
    route.append(people)
    route.append(fishing)
    route.append(0)
    while route:
        a = route.popleft()
        db = route.popleft()
        b = copy.deepcopy(db)
        i = route.popleft()
        while i != 3:
            gate = a[i][0]
            count = a[i][1]
            while count > 0:
                loc = 0
                while count > 0:
                    if loc == 0 and b[gate] == 0:
                        count -= 1
                        b[gate] = loc + 1
                        loc += 1
                    elif count == 1:
                        if gate - loc > 0 and gate + loc < len(b):
                            if b[gate + loc] == 0 and b[gate - loc] == 0:
                                b[gate - loc] = loc + 1
                                count -= 1
                                route.append(a)
                                twob = copy.deepcopy(b)
                                route.append(twob)
                                route.append(i + 1)

                                b[gate - loc] = 0
                                b[gate + loc] = loc + 1
                                break
                            elif b[gate + loc] == 0:
                                b[gate + loc] = loc + 1
                                count -= 1
                                break
                            elif b[gate - loc] == 0:
                                b[gate - loc] = loc + 1
                                count -= 1
                                break
                            else:
                                loc += 1

                        elif gate + loc < len(b) and b[gate + loc] == 0:
                            b[gate + loc] = loc + 1
                            count -= 1
                            break
                        elif gate - loc > 0 and b[gate - loc] == 0:
                            b[gate - loc] = loc + 1
                            count -= 1
                            break
                        else:
                            loc += 1

                    else:
                        if gate - loc > 0 and b[gate - loc] == 0:
                            b[gate - loc] = loc + 1
                            count -= 1
                        elif gate + loc < len(b) and b[gate + loc] == 0:
                            b[gate + loc] = loc + 1
                            count -= 1
                        else:
                            loc += 1
            i += 1
        if mincount > sum(b) - 1:
            mincount = sum(b) - 1


t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(3)]
    mapList = [1] + [0] * n

    mincount = 100000
    for i in itertools.permutations(data, 3):
        dataList = list(i)
        checkRoute(dataList)

    print("#{} {}".format(tc + 1, mincount))
