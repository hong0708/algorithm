ex = ["aya", "ye", "woo", "ma"]


def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        case = ''
        before = ''
        count = True
        for j in range(len(babbling[i])):
            case += babbling[i][j]
            if case in ex and case != before:
                before = case
                case = ''
                count = True
            elif case in ex and case == before:
                count = False
                break
            elif len(case) > 3:
                count = False
                break
            else:
                count = False
        if count:
            answer += 1
    return answer
