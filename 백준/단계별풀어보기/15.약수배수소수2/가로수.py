def check(ar, l):
    for i in range(1, len(ar)):
        if ar[i] - ar[i - 1] != l:
            if l > ar[i] - ar[i - 1]:
                return ar[i] - ar[i - 1]
    return -1


n = int(input())
impl = []
length = 1000000000
for _ in range(n):
    a = int(input())
    if len(impl) > 0:
        length = min(length, a - impl[-1])
    impl.append(a)

arr = [False for _ in range(max(impl) + 1)]
for i in impl:
    arr[i] = True

answer = len(impl)
while True:
    for j in range(impl[0], len(arr), length):
        arr[j] = True
        impl.append(j)
        impl = list(set(impl))

    if check(impl, length) == -1:
        break
    else:
        length = check(impl, length)
print(len(impl) - answer)
