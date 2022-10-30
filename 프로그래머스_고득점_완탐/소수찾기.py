from itertools import permutations


def solution(numbers):
    answer = 0
    new_s = []
    for i in range(1, len(numbers) + 1):
        pm = list(permutations(numbers, i))
        for j in pm:
            num = "".join(j)
            new_s.append(int(num))
    while new_s.count(1):
        new_s.remove(1)
    while new_s.count(0):
        new_s.remove(0)

    new_s = list(set(new_s))
    for i in new_s:
        have = 0
        for j in range(2, i):
            if i % j == 0:
                have += 1
                break
        if have == 0:
            answer += 1
    return answer