x = int(input())

count = 0
i = 0
while x > count:
    count += i
    i += 1
count -= i
i -= 1

a = i + 1
b = 1
for j in range(x - count - 1):
    a -= 1
    b += 1

if i % 2 == 0:
    print(str(a) + '/' + str(b))
else:
    print(str(b) + '/' + str(a))
