from collections import deque
from copy import deepcopy

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def check(x, y):
    c = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            c += 1
    if c > 1:
        return False
    else:
        return True


def find_line(b, t, ws):
    min_count = 1000000

    can_go = deque()
    can_go.append(b)
    can_go.append(0)
    can_go.append(ws)

    while can_go:
        now = can_go.pop()
        count = can_go.pop()
        now_wss = can_go.pop()
        now_ws = deepcopy(now_wss)
        for l in now_wss:
            if check(now, l):
                if l == t:
                    min(min_count, count + 1)
                else:
                    can_go.append(l, count + 1, now_ws.pop(l))


def solution(begin, target, words):
    answer = 0
    find_line(begin, target, words)
    return answer


print(solution(begin, target, words))
