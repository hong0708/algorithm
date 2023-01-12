# https://www.acmicpc.net/problem/4949

while True:
    stack = []
    command = list(input())
    end = True
    if command == '.':
        break

    for i in command:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                end = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                end = False
                break
        elif i == ']':
            if len(stack) == 0:
                end = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                end = False
                break
    if not stack and end:
        print('yes')
    if end == False:
        print('no')
