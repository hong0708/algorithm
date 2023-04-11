def solution(topping):
    map1 = [0 for _ in range(len(topping))]
    map2 = [0 for _ in range(len(topping))]

    count = 0
    brother1 = set()
    brother2 = set()
    for i in range(len(topping)):
        brother1.add(topping[i])
        map1[i] = len(brother1)

    for i in range(len(topping) - 1, -1, -1):
        brother2.add(topping[i])
        map2[i] = len(brother2)

    for i in range(len(topping) - 1):
        if map1[i] == map2[i + 1]:
            count += 1

    return count
