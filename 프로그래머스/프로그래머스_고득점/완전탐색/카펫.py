# 브라운 + 4  /2 = 답 리스트 합 가로2개 세로2개 라는 뜻 범위 줄이기 가능
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