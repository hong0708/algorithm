#https://programmers.co.kr/learn/courses/30/lessons/68936
# return안해서 답 엄청 크게나옴
# 예전에 나왔던 문제라 기억이나서 재귀로 품
def solution(arr):
    answer = [0,0]
    n = len(arr)


    def count(x, y, N):
        who = arr[x][y]
        for i in range(x, x + N):
            for j in range(y, y + N):
                if who != arr[i][j]:
                    slice = N // 2
                    count(x, y, slice)
                    count(x + slice, y + slice, slice)
                    count(x + slice, y, slice)
                    count(x, y + slice, slice)
                    return
        answer[who] += 1


    count(0, 0, n)
    return answer