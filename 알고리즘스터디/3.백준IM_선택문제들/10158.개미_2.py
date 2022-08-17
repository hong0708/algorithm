w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

count = 0
dp = 1
dq = 1

while True:
    if count == t:
        print(p, q)
        break
    if dp > 0 and dq > 0:
        go = min(w - p, h - q)
        if count + go < t:
            count += go
