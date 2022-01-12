#https://programmers.co.kr/learn/courses/30/lessons/62048
#예전 논술문제 비슷한거 있어서 품
#최대공약수 구하는 방법은 이전 문제에서 쓴 방법으로 해결
def solution(w, h):
    answer = 1
    a = 0
    b = 0
    if w > h:
        a = w
        b = h
    else:
        a = h
        b = w
    while b != 0:
        num = b
        b = a % b
        a = num
    if b == 1:
        answer = w * h - w - h + 1
    else:
        answer = w * h - (w + h - a)

    return answer