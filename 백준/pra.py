tmp = "0123456789"

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
def prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        # x가 해당 수로 나누어떨어진다면
        if num % i == 0:
            return False  # 소수가 아님
    return True  # 소수임

arr = [False] * 2  + [True] * 3
print(arr)
answer = 0
convert_num = list(convert(78536544841, 8))
print(convert_num)
a= True
while a:
    while a:
        j = 1
        num = 0
        for i in range(len(convert_num) - 1, -1, -1):
            if i == 0:
                num += int(convert_num[i]) * j
                a = False
                print(num)
                if prime(num):
                    answer += 1
                break

            if convert_num[i] != '0':
                num += int(convert_num[i]) * j

            elif convert_num[i] == '0':
                convert_num = convert_num[:i]
                print(num)
                if prime(num):
                    answer += 1
                break
            j *= 10
print(answer)
