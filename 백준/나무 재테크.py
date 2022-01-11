dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

answer = 0
N, M, K = map(int, input().split())
place = [[5] * N for _ in range(N)]
energy = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
    tree[x - 1][y - 1].sort()

for i in range(K):
    for j in range(N):
        for k in range(N):
            if tree[j][k]:

                # 양분 배분 산나무 죽은나무 나눠서
                newTree, deadTree = [], []
                for z in tree[j][k]:
                    if z <= place[j][k]:
                        place[j][k] -= z
                        z += 1
                        newTree.append(z)
                    elif z > place[j][k]:
                        deadTree.append(z // 2)
                        print(z//2)
                newTree.sort()
                ##print(newTree)
                tree[j][k] = []
                tree[j][k].extend(newTree)
                ##print(sum(deadTree))
                place[j][k] += sum(deadTree)

    if not tree:
        print(0)
        exit()

    # 가을
    for j in range(N):
        for k in range(N):
            if tree[j][k]:
                for z in tree[j][k]:
                    if z % 5 == 0:
                        for seed in range(8):
                            dj = j + dx[seed]
                            dk = k + dy[seed]
                            if 0 <= dj < N and 0 <= dk < N:
                                tree[dj][dk].append(1)
                                tree[dj][dk].sort()

    # 겨울
    for j in range(N):
        for k in range(N):
            place[j][k] += energy[j][k]

for j in range(N):
    for k in range(N):
        if tree[j][k]:
            answer += len(tree[j][k])

print(answer)