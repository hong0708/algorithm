from itertools import permutations

ex = ["aya", "ye", "woo", "ma"]


def solution(babbling):
    answer = 0
    impl = ["aya", "ye", "woo", "ma"]
    for i in range(2, 5):
        for j in permutations(ex, i):
            j = list(j)
            w = ''
            for k in j:
                w += k
            impl.append(w)
    for a in babbling:
        if a in impl:
            answer += 1
    return answer
