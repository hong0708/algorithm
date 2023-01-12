#https://programmers.co.kr/learn/courses/30/lessons/42883
#left를 통해 뽑아야하는 숫자의 수를 통하여 함
#max min이 시간 초과의 원인인듯
number = "199999"
k = 3
answer = ''

num = list(number)

left = len(num) - k
loc = 0

while left > 0:
    if left == 2:
        loc = num.index(max(num[:]))
    else:
        loc = num.index(max(num[:-left+1]))

    answer += num[loc]
    left -= 1
    loc += 1
    num = num[loc:]

print answer
