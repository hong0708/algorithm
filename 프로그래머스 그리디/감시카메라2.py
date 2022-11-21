from itertools import combinations


def solution(routes):
    answer = 0
    nums = []
    for i in routes:
        for j in range(i[0], i[1] + 1):
            if j not in nums:
                nums.append(j)

    for count in range(1, len(nums) + 1):
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
