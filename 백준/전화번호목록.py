t = int(input())
numbers = []


def find_same(numbers):
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i] in numbers[i + 1][0:len(numbers[i])]:
            print("NO")
            return False
    print("YES")
    return True


for _ in range(t):
    n = int(input())

    for _ in range(n):
        numbers.append(input())

    find_same(numbers)
    numbers = []

