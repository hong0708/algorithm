from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    impl = stdin.readline().split()

    if impl[0] == 'push':
        arr.append(impl[1])

    elif impl[0] == 'pop':
        if arr:
            print(arr.pop(0))
        else:
            print(-1)

    elif impl[0] == 'size':
        print(len(arr))

    elif impl[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif impl[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])

    elif impl[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
