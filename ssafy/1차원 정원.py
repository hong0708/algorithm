tc = int(input())
for t in range(tc):
    grass, water = input().split()
    grass = int(grass)
    water = int(water)

    water = water * 2 + 1
    if grass % water == 0:
        count = grass // water
    else:
        count = grass // water + 1

    print("#{} {}".format(t + 1, count))
