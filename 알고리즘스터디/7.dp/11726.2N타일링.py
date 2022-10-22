def sq(n):
    if data[n]:
        return data[n]
    else:
        data[n] = (sq(n - 1) + sq(n - 2)) % 10007
        return data[n]


n = int(input())
data = [0, 1, 2] + [0 for _ in range(1000)]
print(sq(n))
