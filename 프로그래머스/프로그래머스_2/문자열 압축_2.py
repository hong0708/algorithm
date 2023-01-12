#https://programmers.co.kr/learn/courses/30/lessons/60057
#count으로 몇번 반복되는지 확인하고 count자리수 생각해서 자리수측정
def solution(s):
    num = 1
    mini = len(s)
    while True:
        sub = ""
        count = 1
        pre = s[:num]
        for i in range(num, len(s)+ num, num):
            if s[i:i + num] == pre:
                count += 1
            else:
                if count > 1:
                    sub = sub + str(count) + pre
                else:
                    sub = sub + pre
                pre = s[i:i + num]
                count = 1
        if len(sub) < mini:
            mini = len(sub)
        num += 1
        if num > len(s) / 2:
            break
    return mini