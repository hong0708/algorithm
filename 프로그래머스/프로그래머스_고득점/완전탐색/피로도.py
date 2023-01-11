from itertools import permutations


def solution(k, dungeons):
    d_count = len(dungeons)
    d_list = [i for i in range(d_count)]
    for i in range(d_count, 0, -1):
        for c in permutations(d_list, i):
            now = k
            check = True
            for case in c:
                if now < dungeons[case][0]:
                    check = False
                    break
                else:
                    now -= dungeons[case][1]
            if check:
                return i
