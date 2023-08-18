# https://www.acmicpc.net/problem/7662

import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    visited = [False] * k
    arr_min = []
    arr_max = []

    for i in range(k):
        op, n = input().split()
        n = int(n)

        if op == 'I':
            heapq.heappush(arr_min, (n, i))
            heapq.heappush(arr_max, (n * -1, i))
        else:
            # 최댓값 삭제
            if n == 1:
                # 아직 방문 하지 않은 값이 나올 때 까지 제거해줘야한다
                while arr_max and visited[arr_max[0][1]]:
                    heapq.heappop(arr_max)
                if arr_max:
                    visited[arr_max[0][1]] = True
                    heapq.heappop(arr_max)
            # 최솟값 삭제
            else:
                while arr_min and visited[arr_min[0][1]]:
                    heapq.heappop(arr_min)
                if arr_min:
                    visited[arr_min[0][1]] = True
                    heapq.heappop(arr_min)

    # 이미 방문해서 제거해야하는 숫자가 남아있다면 제거가 추가적으로 필요하다
    while arr_max and visited[arr_max[0][1]]:
        heapq.heappop(arr_max)
    while arr_min and visited[arr_min[0][1]]:
        heapq.heappop(arr_min)

    if arr_min and arr_max:
        print(arr_max[0][0] * -1, arr_min[0][0])
    else:
        print('EMPTY')

