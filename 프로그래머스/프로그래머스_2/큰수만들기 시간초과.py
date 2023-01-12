#https://programmers.co.kr/learn/courses/30/lessons/42883
#반복문을 통해 숫자를 num에 넣고 비교하며 작은 수면 제외 시켜 k감소
def solution(number, k):
    num = ''
    for i in range(len(number)):
        while num and num[-1] < number[i] and k > 0:
            if len(num) == 1:
                num = ''
                k -= 1
                break
            else:
                num = num[:-1]
                k -= 1
        if k == 0:
            num += number[i:]
            break
        num += number[i]
    if k > 0:
        num = num[:-k]

    return num