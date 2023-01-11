def solution(clothes):
    answer = 1
    case = {}

    for i in clothes:
        if i[1] in case:
            case[i[1]] += 1
        else:
            case[i[1]] = 1

    for i in case:
        answer *= (case[i] + 1)

    answer -= 1

    return answer
