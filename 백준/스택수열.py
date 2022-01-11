n = int(input())
stack = []
result = []
count = 0
answer = True
for _ in range(n):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        answer = False
        break
if answer == False:
    print ("NO")
else:
    for i in result:
        print (i)
