#https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    answer = 100
    a = 0
    b = 1
    if n == 2:
        answer == b
    else:
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        answer = c % 1234567
    return answer