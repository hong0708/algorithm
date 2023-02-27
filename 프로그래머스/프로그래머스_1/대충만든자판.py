def solution(keymap, targets):
    answer = []
    for a in range(len(keymap)):
        keymap[a] = list(keymap[a])

    for i in targets:
        i = list(i)
        total = 0
        for j in i:
            notIn = True
            minCount = 101
            for a in range(len(keymap)):
                if j in keymap[a]:
                    minCount = min(minCount, keymap[a].index(j) +1)
                    notIn = False
            if notIn:
                answer.append(-1)
                break
            else:
                total += minCount
        if minCount != 101:
            answer.append(total)
    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
