import copy


def solution(n, wires):
    answer = 100

    for i in range(len(wires)):
        imp = copy.deepcopy(wires)
        imp.pop(i)
        a = []
        b = []
        count = 0
        while imp:
            now = imp.pop(0)
            if count == len(wires) + 1:
                b.append(now[0])
                b.append(now[1])
                count = 0

            if len(a) == 0 and len(b) == 0:
                a.append(now[0])
                a.append(now[1])
            else:
                if now[0] in a:
                    a.append(now[1])
                    count = 0
                elif now[1] in a:
                    a.append(now[0])
                    count = 0
                elif now[0] in b:
                    b.append(now[1])
                    count = 0
                elif now[1] in b:
                    b.append(now[0])
                    count = 0
                else:
                    imp.append(now)
                    count += 1
        a = set(a)
        b = set(b)

        if len(b) == 0:
            now_num = abs(len(a) - len(b)) - (n - len(a))
        else:
            now_num = abs(len(a) - len(b))
        answer = min(answer, now_num)
    return answer