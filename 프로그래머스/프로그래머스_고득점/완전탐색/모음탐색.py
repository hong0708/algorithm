from itertools import product


def solution(word):
    words = ["A", "E", "I", "O", "U"]
    lists = []

    for i in range(1, 6):
        imp = ""
        for j in product(words, repeat=i):
            j = list(j)
            imp = ''.join(str(s) for s in j)
            lists.append(imp)
    lists.sort()

    return lists.index(word) + 1