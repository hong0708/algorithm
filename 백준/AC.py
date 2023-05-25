from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    q = deque(arr)

    flag = 0

    if n == 0:
        q = []

    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(q) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    else:
        if flag % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")