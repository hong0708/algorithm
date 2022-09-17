prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # 우선순위

for tc in range(10):
    n = int(input())
    arr = input()

    postFix = []
    operatorStack = []

    for i in range(n):
        if arr[i].isdigit():
            postFix.append(arr[i])
        elif arr[i] == '(':
            operatorStack.append(arr[i])
        elif arr[i] == ')':
            while operatorStack[-1] != '(':
                postFix.append(operatorStack.pop())
            if operatorStack[-1] == '(':
                operatorStack.pop()
        else:
            while operatorStack and prior[arr[i]] <= prior[operatorStack[-1]]:
                postFix.append(operatorStack.pop())
            operatorStack.append(arr[i])
    while operatorStack:
        postFix.append(operatorStack.pop())

    numStack = []  # 숫자 추가 리스트
    num1 = 0
    num2 = 0
    for j in range(len(postFix)):
        if postFix[j].isdigit():
            numStack.append(int(postFix[j]))
        elif postFix[j] == '+':
            num1 = numStack.pop()
            num2 = numStack.pop()
            numStack.append(num1 + num2)
        elif postFix[j] == '-':
            num1 = numStack.pop()
            num2 = numStack.pop()
            numStack.append(num1 - num2)
        elif postFix[j] == '*':
            num1 = numStack.pop()
            num2 = numStack.pop()
            numStack.append(num1 * num2)
        elif postFix[j] == '/':
            num1 = numStack.pop()
            num2 = numStack.pop()
            numStack.append(num1 / num2)

    print("#{} {}".format(tc + 1, numStack[0]))
