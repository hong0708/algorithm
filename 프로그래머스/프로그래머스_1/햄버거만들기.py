def check(s):
    test = [1, 3, 2, 1]
    for i in range(4):
        if test[i] != s[len(s) - i - 1]:
            return False
    return True


def solution(ingredient):
    answer = 0
    s = []
    for i in range(len(ingredient)):
        s.append(ingredient[i])
        if ingredient[i] == 1 and len(s) > 3:
            if check(s):
                s.pop()
                s.pop()
                s.pop()
                s.pop()
                answer += 1

    return answer
