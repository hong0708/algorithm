n = int(input())
impl = []
length = 1000000000
for _ in range(n):
    a = int(input())
    if len(impl) > 0:
        length = min(length, a - impl[-1])
    impl.append(a)

for i in range(1, len(impl)):
    impl[i] -= impl[0]
impl[0] = 0

while True:
    end = True
    for j in impl:
        if j % length != 0:
            end = False
            length -= 1
            break
    if end:
        break
print(max(impl) // length - len(impl) + 1)
