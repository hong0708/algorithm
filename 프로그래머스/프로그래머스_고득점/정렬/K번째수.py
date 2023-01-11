def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        pre = []
        for j in range(commands[i][0] - 1, commands[i][1]):
            pre.append(array[j])
        pre.sort()
        answer.append(pre[commands[i][2]-1])
    return answer