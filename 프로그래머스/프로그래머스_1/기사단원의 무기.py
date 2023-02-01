def solution(number, limit, power):
    answer = 0
    imp = [0 for _ in range(number + 1)]

    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            imp[j] += 1

    for a in range(1, number + 1):
        if imp[a] > limit:
            answer += power
        else:
            answer += imp[a]
    return answer
