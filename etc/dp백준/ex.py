import sys

x = int(input())
print (x // 2)
number = list(map(int, sys.stdin.readline().split()))
answer = int(input())

if answer in number:
    print (number.index(answer))
else:
    print ('n')

while True:
    if x == 1 and answer != number[x // 2]:
        print ('n')
        break

    if answer > number[x // 2]:
        number = number[x // 2:]
        x = x // 2
    elif answer < number[x // 2]:
        number = number[:x // 2]
        x = x // 2
    if answer == number[x // 2]:
        print (x//2)
        break
