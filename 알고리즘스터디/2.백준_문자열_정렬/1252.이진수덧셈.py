a, b = map(str, input().split())
a = '0b' + a
b = '0b' + b

a = int(a, 2)
b = int(b, 2)
c = bin(a + b)
c = str(c)
c = c[2:]
print(c)
