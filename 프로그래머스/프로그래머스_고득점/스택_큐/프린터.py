def solution(priorities, location):
    count = 1
    while len(priorities):
        if location != 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities[0])
                priorities.pop(0)
                location -= 1
            else:
                priorities.pop(0)
                location -= 1
                count += 1
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities[0])
                priorities.pop(0)
                location = len(priorities) - 1
            else:
                break
    return count
