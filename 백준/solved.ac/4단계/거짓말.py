# https://www.acmicpc.net/problem/1043

from collections import deque

n, m = map(int, input().split())
tt = list(map(int, input().split()))
t_people = set(tt[1:])
f_people = set()
party = [[] for _ in range(m)]
ans = 0

for i in range(m):
    impl = list(map(int, input().split()))
    impl = impl[1:]
    impl.sort()
    party[i] += impl

dq = deque()
dq.append([0, t_people, f_people, 0])
while dq:
    now = dq.popleft()
    loc, t, f = now[0], now[1], now[2]

    if loc == m:
        if t & f:
            continue
        ans = max(ans, now[3])
    else:
        p = set(party[loc])
        # 둘 다 속하며 거짓말 들킴 불가능한 경우
        if p & t and p & f:
            continue
        # 진실을 아는 사람이 있다는 것
        # 진실을 말하고 진실을 아는사람들로 추가해야함
        if p & t:
            dq.append([loc + 1, p | t, f, now[3]])
        # 거짓을 아는 사람이 있음
        # 거짓으로 말하고 거짓으로 추가하기
        elif p & f:
            dq.append([loc + 1, t, p | f, now[3] + 1])
        else:
            dq.append([loc + 1, t, p | f, now[3] + 1])
            dq.append([loc + 1, p | t, f, now[3]])
print(ans)
