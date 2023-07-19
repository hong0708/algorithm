# https://www.acmicpc.net/problem/4779
while True:
    try:
        n = int(input())
        arr = '-'
        count = 0
        while count != n:
            arr = arr + ' ' * len(arr) + arr
            count += 1

        print(arr)
    except:
        break
