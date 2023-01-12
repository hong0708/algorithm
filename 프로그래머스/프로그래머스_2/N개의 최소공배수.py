#https://programmers.co.kr/learn/courses/30/lessons/12953
#어짜피 최소 공배수라 가장 큰 수의 배수로 해결
def solution(arr):
    answer = 0
    a = max(arr)
    mul = 1
    b = True
    while b:
        for i in range(len(arr)):
            if (a * mul) % arr[i] != 0:
                break
            if i == len(arr) -1 and (a * mul) % arr[i] == 0:
                b = False
        mul += 1
    answer = a * (mul - 1)
    return answer