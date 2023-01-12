#https://programmers.co.kr/learn/courses/30/lessons/68645
#전에 했던 문제라 쉽게품
def solution(n):
    answer = []
    list = [[0 for _ in range(n)] for _ in range(n)]
    a = -1
    b = 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                a += 1
            elif i % 3 == 1:
                b += 1
            elif i % 3 == 2:
                a -= 1
                b -= 1
            list[a][b] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if list[i][j] != 0:
                answer.append(list[i][j])
    return answer