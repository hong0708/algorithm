from itertools import combinations


def makeList():
    return 0


def solution(routes):
    answer = 0

    for count in range(1, len(routes) + 1):
        for cam in combinations(routes, count):
            cam = list(cam)
            for a in range(len(cam)):
                for b in range(cam[a][0] + 1, cam[a][1]):
                    cam[a].append(b)
                cam[a] = sorted(cam[a])
            print(cam)

            cam_list = []
            for t in range(count):
                for one in combinations(cam[t], 1):
                    cam_list.append(one)

    return answer


r = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

print(solution(r))
