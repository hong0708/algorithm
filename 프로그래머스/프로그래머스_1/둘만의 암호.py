from copy import deepcopy

alpa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]


def solution(s, skip, index):
    answer = ''
    temp = deepcopy(alpa)
    for i in skip:
        temp.pop(temp.index(i))
    s = list(s)
    for j in range(len(s)):
        s[j] = temp[(temp.index(s[j]) + index) % len(temp)]
    answer = ''.join(map(str, s))
    return answer


print(solution("aukks", "wbqd", 5))
