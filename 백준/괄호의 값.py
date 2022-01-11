all = [input()]

open = []
count = 0

for i in range(len(all)):
    if all[i] == "(" or all[i] == "[":
        open.append(all[i])
    elif all[i] == ")":
        if open[-1] != "(":
            print(0)
            break
        else:
            if len(open) == 1:

    elif all[i] == "]":
        if open[-1] != "[":
            print(0)
            break
