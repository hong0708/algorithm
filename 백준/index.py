double = []
for i in range(1, 101):
    double.append(i * i)

m = int(input())
n = int(input())

double.append(m)
double.append(n)
double.sort()
M = double.index(m)
N = double.index(n)
count = 0
if N-M == 1:
    print(-1)
else:
    if double.count(n) != 1:
        for i in range(M + 1, N + 1):
            count += double[i]
        print(count)
        print(double[M + 1])
    else:
        for i in range(M + 1, N):
            count += double[i]
        print(count)
        print(double[M + 1])
