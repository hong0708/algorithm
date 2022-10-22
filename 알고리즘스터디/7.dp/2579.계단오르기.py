def work(n):
    if records[n][0] != 0 or records[n][0] != 0:
        answer[n] = max(records[n][0], records[n][1])
        return
    else:
        work(n - 2)
        work(n - 1)
        records[n][1] = max(records[n - 2][0], records[n - 2][1]) + data[n]
        records[n][0] = records[n - 1][1] + data[n]
        answer[n] = max(records[n][0], records[n][1])


n = int(input())
data = [0]

for _ in range(n):
    data.append(int(input()))
if n == 1:
    print(data[1])
else:
    # 0 1걸음, 1 2걸음
    records = [[0, 0], [data[1], 0], [data[1] + data[2], data[2]]] + [[0, 0] for _ in range(n)]
    answer = [0 for _ in range(n + 1)]
    work(n)
    print(answer[n])
