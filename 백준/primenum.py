n = int(input())
a = [False, False] + [True] * (n - 1)
primes = []
count = 0
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

for i in range(len(primes)):
    add = 0
    for j in range(i, len(primes)):
        add += primes[j]
        if n == add:
            count += 1
            break
        if n < add:
            break
print(count)