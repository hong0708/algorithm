#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    long = len(s)
    num = 1
    mini = long
    while True:
        a = long
        i = 0
        same = 0
        while True:
            if i + num > long:
                if same > 0:
                    same += 1
                    many = str(same)
                    a = a - (same * num) + len(many) + num
                    same = 0
                if a < mini:
                    mini = a
                break
            if s[i:i + num] != s[i + num:i + 2 * num]:
                i += num
                if same > 0:
                    same += 1
                    many = str(same)
                    a = a - (same * num) + len(many) + num
                    same = 0
            elif s[i:i + num] == s[i + num:i + 2 * num]:
                i += num
                same += 1
        num += 1
        if num > long/2:
            break
    return mini