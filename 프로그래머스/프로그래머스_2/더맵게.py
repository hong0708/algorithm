import heapq


def solution(S, K):
    heap = []
    for i in S:
        heapq.heappush(heap, i)

    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        cnt += 1
    return cnt
