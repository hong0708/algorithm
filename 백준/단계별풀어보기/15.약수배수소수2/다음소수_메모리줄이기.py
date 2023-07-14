def check(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
impl = []
for _ in range(n):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        if check(num):
            print(num)
            break
        else:
            num += 1
