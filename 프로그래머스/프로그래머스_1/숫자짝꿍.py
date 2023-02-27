def solution(X, Y):
    X = list(X)
    Y = list(Y)

    l = max(len(X), len(Y))
    impX = [0 for _ in range(10)]
    impY = [0 for _ in range(10)]
    temp = []

    for i in range(l):
        if i < len(X):
            impX[int(X[i])] += 1
        if i < len(Y):
            impY[int(Y[i])] += 1

    for i in range(10):
        for j in range(min(impX[i], impY[i])):
            temp.append(i)
    if len(temp) == 0:
        return '-1'
    elif sum(temp) == 0:
        return '0'
    else:
        temp.sort(reverse=True)
        return ''.join(map(str, temp))


print(solution("100", "123450"))
