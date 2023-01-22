from itertools import permutations


def solution(dots):
    answer = 0
    dots.sort(key=lambda x: x[0])

    for case in permutations([0, 1, 2, 3], 4):
        c = list(case)
        x = (dots[c[0]][0] - dots[c[1]][0]) / (dots[c[0]][1] - dots[c[1]][1])
        y = (dots[c[2]][0] - dots[c[3]][0]) / (dots[c[2]][1] - dots[c[3]][1])
        if x == y:
            answer = 1
            break

    return answer


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
