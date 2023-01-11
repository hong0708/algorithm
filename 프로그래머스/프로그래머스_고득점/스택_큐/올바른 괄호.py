def solution(s):
    answer = True
    num = 0
    left = 0
    right = 0
    while num < len(s):
        if s[num] == '(':
            left += 1
        elif s[num] == ')':
            right += 1

        if right > left:
            answer = False
            break
        if num == len(s) - 1 and left != right:
            answer = False
            break
        num += 1

    return answer
