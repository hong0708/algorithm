# https://www.acmicpc.net/problem/1918

from collections import deque

arr = input()
ans = ''

num = deque()
cal = deque()

for i in arr:
    if i.isalpha():
        ans += i
    else:
        if i == "*":
            # * / 는 같은 우선순위로 이 경우만 먼저 미리 추가한다
            while cal and (cal[-1] == '*' or cal[-1] == '/'):
                ans += cal.pop()
            cal.append(i)
        elif i == "/":
            # * / 는 같은 우선순위로 이 경우만 먼저 미리 추가한다
            while cal and (cal[-1] == '*' or cal[-1] == '/'):
                ans += cal.pop()
            cal.append(i)

        elif i == "+":
            # 우선순위가 제일 낮기 때문에 먼저 이전 연산자들을 추가
            while cal and cal[-1] != '(':
                ans += cal.pop()
            # 그리고 본인을 스택에 추가
            cal.append(i)
        elif i == "-":
            # 우선순위가 제일 낮기 때문에 먼저 이전 연산자들을 추가
            while cal and cal[-1] != '(':
                ans += cal.pop()
            # 그리고 본인을 스택에 추가
            cal.append(i)

        elif i == "(":
            # 일단 추가해준다.
            cal.append(i)
        elif i == ")":
            # ( 까지 결과에 추가해준다)
            while cal and cal[-1] != '(':
                ans += cal.pop()
            # ( 까지 마지막으로 제거
            cal.pop()

while cal:
    ans += cal.pop()
print(ans)
