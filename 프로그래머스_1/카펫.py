#https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    a = 3
    while True:
        if total % a == 0:
            if brown == 2 * a + (total/a) * 2 - 4:
                break
        a += 1
    if a > total/a:
        answer.append(a)
        answer.append(total/a)
    else :
        answer.append(total/a)
        answer.append(a)
    return answer