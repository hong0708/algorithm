p = 5
l = 5

point = [1, 3, 10, 20, 30]

one, two = 4,8
where = []
where.append(point)
where.append(one)
where.append(two)

count = 0
where.sort()
if where.count(two) == 2:
    count += 1

count += where.index(two) - where.index(one)
#point = point[:-2]
print (count - 1)
print (point)
