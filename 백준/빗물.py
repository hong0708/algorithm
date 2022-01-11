w, h = map(int, input().split())
raindrop = list(map(int, input().split()))
longline = max(raindrop)
where = raindrop.index(longline)

total = 0
up = 0
for i in range(where + 1):
    if raindrop[i] > up:
        up = raindrop[i]
    total += up
up = 0
for j in range(len(raindrop) - 1, where, -1):
    if raindrop[j] > up:
        up = raindrop[j]
    total += up
print(total - sum(raindrop))
