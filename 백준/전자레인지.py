a, A = 300, 0
b, B = 60, 0
c, C = 10, 0

time = int(input())
A = time // a
if time // a != 0:
    time = time % a
B = time // b
if time // b != 0:
    time = time % b
C = time // c
if time % c != 0:
    print(-1)
else:
    print(str(A) + ' ' + str(B) + ' ' + str(C))
