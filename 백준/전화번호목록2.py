def cal(a):
    for j in range(len(a) - 1):
        if a[j] == a[j + 1][:len(a[j])]:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []

    for i in range(n):
        arr.append(input())
    arr.sort()
    print(cal(arr))
