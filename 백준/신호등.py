n, l = map(int, input().split())
time = 0
loc = 0

for _ in range(n):
    d, r, g = map(int, input().split())
    time += (d - loc)
    if time % (r + g) <= r:
        time += (r - (time % (r + g)))
    loc = d

time += (l - loc)
print(time)
