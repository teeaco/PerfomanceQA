mass = []
for i in range(5):
    a = int(input())
    mass += [a]
mass.sort()
for i in range(4, -1, -1):
    print(mass[i])