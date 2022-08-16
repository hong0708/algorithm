w, h = map(int, input().split())
count = int(input())
wList = []
hList = []
for i in range(count):
    data = list(map(int, input().split()))
    if data[0] == 1:
        wList.append(data[1])
    else:
        hList.append(data[1])
wList.sort()
hList.sort()

wList.append(w)
hList.append(h)

maxW = 0
maxH = 0

preLoc = 0
for i in range(len(wList)):
    if wList[i] - preLoc > maxW:
        maxW = wList[i] - preLoc
    preLoc = wList[i]
preLoc = 0
for i in range(len(hList)):
    if hList[i] - preLoc > maxH:
        maxH = hList[i] - preLoc
    preLoc = hList[i]
print(maxW * maxH)
