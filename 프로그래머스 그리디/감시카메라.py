from itertools import combinations


def solution(routes):
    answer = 0

    min_loc = 30000
    max_loc = -30000
    for i in routes:
        min_loc = min(min_loc, i[0])
        max_loc = max(max_loc, i[1])

    nums = []

    for j in range(min_loc, max_loc + 1):
        nums.append(j)

    print(nums)
    for count in range(1, max_loc - min_loc + 1):
        for cam in combinations(nums, count):
            cam = list(cam)
            print(cam)
            isIn = False
            get = False
            # routes list check
            for t in range(len(routes)):

                isIn = False
                # cam list check
                for k in range(len(cam)):
                    if routes[t][0] <= cam[k] <= routes[t][1]:
                        isIn = True
                        break

                if not isIn:
                    break

                if isIn and t == len(routes) - 1:
                    get = True
            if get:
                answer = count
                break

        if answer:
            break
    return answer


r = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

print(solution(r))
