k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
start = 1
end = max(lines)
while (start <= end):
    center = (start + end) // 2
    count = 0
    for i in lines:
        count += i // center
    if count >= n:
        start = center + 1
    else:
        end = center - 1
print(end)
