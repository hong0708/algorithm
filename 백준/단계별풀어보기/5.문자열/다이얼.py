alp = str(input())

NUM = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for j in range(len(alp)):
    for i in range(len(NUM)):
        if alp[j] in NUM[i]:
            time += NUM.index(NUM[i]) + 3
print(time)
