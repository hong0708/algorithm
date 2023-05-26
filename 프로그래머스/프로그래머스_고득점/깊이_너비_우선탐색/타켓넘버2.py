from itertools import combinations


def c(a):
    i = []
    for t in range(len(a)):
        i.append(a[t])
    return i


def solution(numbers, target):
    answer = 0
    arr = [i for i in range(len(numbers))]

    for j in range(len(numbers)):
        for k in combinations(arr, j + 1):
            impl = c(numbers)
            k = list(k)
            for l in range(len(k)):
                impl[k[l]] *= -1
            if sum(impl) == target:
                answer += 1
    return answer


print(solution([1, 1, 1, 1, 1], 3))
