import itertools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = 0

# 6개를 중복을 허용하여 숫자 뽑기
for six_numbers in itertools.combinations_with_replacement(numbers, 6):
    # 6개의 숫자를 순열 나열하여 모든 경우 체크
    for case in itertools.permutations(six_numbers, 6):
        # 절반으로 잘라서 검사
        # 순열로 모든 케이스 확인하기 때문에 가능
        first = False
        second = False

        if case[0] == case[1] == case[2]:
            first = True
        if case[0] - case[1] == 1 and case[1] - case[2] == 1:
            first = True

        if case[3] == case[4] == case[5]:
            first = True
        if case[3] - case[4] == 1 and case[4] - case[5] == 1:
            first = True
