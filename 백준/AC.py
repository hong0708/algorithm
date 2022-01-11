num = int(input())
dir = 0

for _ in range(num):
    for _ in range(3):
        commend = input()
        list_len = int(input())
        num_list = input().rstrip()[1:-1].split(",")

        for i in range(len(commend)):
            if commend[i] == 'R':
                if dir == 0:
                    dir = 1
                else:
                    dir = 0

            if commend[i] == 'D':
                if dir == 0:
                    num_list = num_list[1:]
                    if len(num_list) < 1:
                        print("error")
                        dir = 0
                        break
                else:
                    num_list = num_list[:-1]
                    if len(num_list) < 1:
                        print("error")
                        dir = 0
                        break
        if len(num_list) > 0:
            if dir == 0:
                print(num_list)
                dir = 0
            else:
                num_list.reverse()
                print(num_list)
                dir = 0
