people = int(input())
cute = 0
n_cute = 0
for _ in range(people):
    q = int(input())
    if q == 0:
        n_cute += 1
    else:
        cute += 1
if cute > n_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")