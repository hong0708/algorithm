# https://www.acmicpc.net/problem/9019

from collections import deque

t = int(input())

for _ in range(t):
    visited = [False for _ in range(10000)]
    a, b = input().split()
    b = int(b)
    dq = deque()
    dq.append([a, ''])

    while dq:
        now = dq.popleft()
        num, com = now[0], now[1]
        visited[int(num)] = True

        if int(num) == b:
            print(com)
            break
        else:
            d = int(num) * 2 % 10000
            if not visited[d]:
                visited[d] = True
                dq.append([str(d), com + 'D'])

            if int(num) == 0:
                s = 9999
            else:
                s = int(num) - 1
            if not visited[s]:
                visited[s] = True
                dq.append([str(s), com + 'S'])

            if len(num) != 4:
                l = ''
                for _ in range(4 - len(num)):
                    l += '0'
                l += num
                l = l[1:] + l[0]
            else:
                l = num[1:] + num[0]
            if not visited[int(l)]:
                visited[int(l)] = True
                dq.append([l, com + 'L'])

            if len(num) != 4:
                r = ''
                for _ in range(4 - len(num)):
                    r += '0'
                r += num
                r = r[-1] + r[0:3]
            else:
                r = num[-1] + num[0:3]
            if not visited[int(r)]:
                visited[int(r)] = True
                dq.append([r, com + 'R'])
