#https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    a = x
    b = 0
    while a > 0:
        c = a % 10
        b += c
        a = a // 10
    if x % b != 0:
        answer = False
    return answer