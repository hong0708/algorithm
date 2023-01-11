def solution(bridge_length, weight, truck_weights):
    answer = 0
    on = []
    finish = []
    count = []
    while len(truck_weights) > 0:
        answer += 1
        if count:
            for i in range(len(count)):
                count[i] += 1

        if count and count[0] == bridge_length:
            if on[0]:
                finish.append(on[0])
                on.pop(0)
                count.pop(0)

        if sum(on) + truck_weights[0] <= weight:
            on.append(truck_weights[0])
            truck_weights.pop(0)
            count.append(0)
    answer += (bridge_length)
    return answer
