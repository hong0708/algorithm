#https://programmers.co.kr/learn/courses/30/lessons/17681
# | 연산자의 사기성
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = arr1[i] | arr2[i]
        j = n - 1
        temp = ""
        while (j >= 0):
            if a % 2 == 1:
                temp = "#" + temp
            elif a % 2 == 0:
                temp = " " + temp
            a //= 2
            j -= 1
        answer.append(str(temp))
    return answer