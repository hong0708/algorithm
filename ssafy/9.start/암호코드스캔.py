hTob = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

bTod = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4, '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9}

bTod_noz = {'211': 3, '221': 2, '122': 2, '411': 1, '132': 1, '231': 1, '114': 1, '312': 1, '213': 1, '112': 3}


def checkCode(code):
    if ((code[7] + code[5] + code[3] + code[1]) * 3 + code[6] + code[4] + code[2] + code[0]) % 10 == 0:
        return True
    else:
        return False


t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    arr = list(input()[:m] for _ in range(n))

    maxMulti = m * 4 // 56

    for i in range(n):
        oneLine = ''
        for j in arr[i]:
            oneLine += hTob[j]
        arr[i] = oneLine

    visited_code = []

    for a in range(n):
        z_o1 = 0
        z_o2 = 0
        z_o3 = 0
        z_o4 = 0
        result = []
        if '1' not in arr[a]:
            continue

        for b in range(m * 4 - 1, -1, -1):

            if z_o3 == 0 and arr[a][b] == '1':
                z_o4 += 1
            elif z_o2 == 0 and z_o4 != 0 and arr[a][b] == '0':
                z_o3 += 1
            elif z_o1 == 0 and z_o4 != 0 and arr[a][b] == '1':
                z_o2 += 1
            elif z_o2 != 0 and arr[a][b] == '0':

                multi = min(z_o4, z_o3, z_o2)

                if multi <= maxMulti:
                    if z_o4 % multi == 0 and z_o3 % multi == 0 and z_o2 % multi == 0:
                        if str(z_o2 // multi) + str(z_o3 // multi) + str(z_o4 // multi) in bTod_noz:

                            zCount = bTod_noz[str(z_o2 // multi) + str(z_o3 // multi) + str(z_o4 // multi)]

                            checkZ = True
                            for c in range(b, b - zCount * multi, -1):
                                if arr[a][c] != '0':
                                    checkZ = False
                                    break

                            if checkZ:
                                result.append(bTod[str(zCount) + str(z_o2 // multi) + str(z_o3 // multi) + str(
                                    z_o4 // multi)])

                z_o1 = z_o2 = z_o3 = z_o4 = 0

                if len(result) == 8:
                    if result not in visited_code:
                        if checkCode(result):
                            visited_code.append(result)
                            answer += sum(result)

                    result = []
    print("#{} {}".format(tc, answer))
