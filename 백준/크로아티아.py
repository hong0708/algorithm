cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input()

for i in cro:
    x = x.replace(i, 'a')
print(len(x))
