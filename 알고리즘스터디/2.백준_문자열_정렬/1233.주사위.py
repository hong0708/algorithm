s1, s2, s3 = map(int, input().split())
addList = list(0 for i in range(s1 + s2 + s3 + 1))

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            addList[i + j + k] += 1
print(addList.index(max(addList)))
