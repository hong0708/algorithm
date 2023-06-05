arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
s = ''

while N:
    s += str(arr[N % B])
    N //= B

print(s[::-1])
