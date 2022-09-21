from itertools import combinations

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]


def charge(a, b):
    global charge_max
    case_a = []
    case_b = []
    now_charge = 0
    for i in range(len(bc)):
        if abs(bc[i][1] - 1 - a[0]) + abs(bc[i][0] - 1 - a[1]) <= bc[i][2]:
            case_a.append(i)
        if abs(bc[i][1] - 1 - b[0]) + abs(bc[i][0] - 1 - b[1]) <= bc[i][2]:
            case_b.append(i)
    if case_a and case_b:
        # 모든 베터리경우 비교 후 가장 큰 값으로
        for a_bc_list in combinations(case_a, 1):
            for b_bc_list in combinations(case_b, 1):
                a_bc_list = list(a_bc_list)
                b_bc_list = list(b_bc_list)

                a_bc = a_bc_list[0]
                b_bc = b_bc_list[0]

                charge = 0
                if a_bc == b_bc:
                    charge = bc[a_bc][3]
                else:
                    charge += bc[a_bc][3]
                    charge += bc[b_bc][3]
                now_charge = max(charge, now_charge)
    elif case_a:
        for a_bc_list in combinations(case_a, 1):
            a_bc_list = list(a_bc_list)
            a_bc = a_bc_list[0]
            charge = 0
            charge += bc[a_bc][3]
            now_charge = max(charge, now_charge)
    elif case_b:
        for b_bc_list in combinations(case_b, 1):
            b_bc_list = list(b_bc_list)
            b_bc = b_bc_list[0]

            charge = 0
            charge += bc[b_bc][3]
            now_charge = max(charge, now_charge)
    charge_max += now_charge


t = int(input())
for tc in range(1, t + 1):
    # m 이동시간 a BC개수
    m, cnt_bc = map(int, input().split())
    dir_a = list(map(int, input().split()))
    dir_b = list(map(int, input().split()))
    charge_max = 0
    bc = []
    for i in range(cnt_bc):
        bc.append(list(map(int, input().split())))
    loc_a = [0, 0]
    loc_b = [9, 9]

    for time in range(m + 1):
        # 초기 시작할 때 충전
        if time == 0:
            charge(loc_a, loc_b)
        else:
            # 이동 이후 충전
            loc_a[0] = loc_a[0] + dx[dir_a[time - 1]]
            loc_a[1] = loc_a[1] + dy[dir_a[time - 1]]

            loc_b[0] = loc_b[0] + dx[dir_b[time - 1]]
            loc_b[1] = loc_b[1] + dy[dir_b[time - 1]]

            charge(loc_a, loc_b)
    print("#{} {}".format(tc, charge_max))
