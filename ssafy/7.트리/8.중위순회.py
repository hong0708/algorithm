def inorder(a):
    if a <= n:
        inorder(a * 2)
        print(data[a], end='')
        inorder(a * 2 + 1)


for t in range(10):
    n = int(input())
    data = [0] * (n + 1)
    for i in range(n):
        words = list(input().split())
        data[i + 1] = words[1]
    print("#{}".format(t + 1, end=''))
    inorder(1)
    print()
