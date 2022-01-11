# https://www.acmicpc.net/problem/1003
a = int(input())
def cal(num):
    zero = [1, 0]
    one = [0, 1]
    answer = [0, 0]
    if num == 0:
        for i in zero:
            print(i, end=' ')
    elif num == 1:
        for i in one:
            print(i, end=' ')

    else:
        for _ in range(num - 1):
            answer = [0, 0]
            answer[0] = zero[0] + one[0]
            answer[1] = zero[1] + one[1]
            zero = one
            one = answer
        for i in answer:
            print(i, end=' ')


for i in range(a):
    k = int(input())
    cal(k)
