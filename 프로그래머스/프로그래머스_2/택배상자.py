def solution(order):
    answer = 0
    extra = []
    loc = 1

    while True:
        if loc == len(order) + 1:
            break

        extra.append(loc)
        if extra and extra[-1] == order[answer]:
            while True:
                if extra and extra[-1] == order[answer]:
                    answer += 1
                    extra.pop()
                else:
                    break
        loc += 1

    return answer
