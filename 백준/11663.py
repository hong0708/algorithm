p, l = map(int, input().split())
point = [map(int, input().split())]

for _ in range(l):
    line = [map(int, input().split())]
    where = []
    where = point
    where.append(line[0])
    where.append(line[1])

    where.sort()

    count = where.index(line[1]) - where.index(line[0])
    print (count)