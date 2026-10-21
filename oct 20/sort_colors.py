n = int(input("Enter size: "))
colors = []

for i in range(n):
    x = int(input("Enter color (0, 1 or 2): "))
    colors.append(x)

zero = 0
one = 0
two = 0

for x in colors:
    if x == 0:
        zero += 1
    elif x == 1:
        one += 1
    else:
        two += 1

pos = 0

while zero > 0:
    colors[pos] = 0
    pos += 1
    zero -= 1

while one > 0:
    colors[pos] = 1
    pos += 1
    one -= 1

while two > 0:
    colors[pos] = 2
    pos += 1
    two -= 1

print("Sorted colors:", colors)