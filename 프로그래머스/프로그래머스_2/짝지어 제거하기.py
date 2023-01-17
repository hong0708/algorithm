def solution(s):
    s = list(s)
    temp = []
    for i in range(len(s)):
        if len(temp) == 0:
            temp += s[i]
        elif temp[-1] == s[i]:
            temp.pop()
        else:
            temp += s[i]
    if len(temp) == 0:
        return 1
    else:
        return 0