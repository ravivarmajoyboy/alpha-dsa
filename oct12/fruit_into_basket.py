c = int(input("enter the total number: "))
d = []
for e in range(c):
    d.append(int(input("enter the fruit: ")))

best = 0
f = 0
g = 0
one = d[0]
two = -1
run = 0

while g < c:
    if d[g] == one:
        run = run + 1
    elif d[g] == two:
        two = one
        one = d[g]
        run = 1
    else:
        f = g - run
        two = one
        one = d[g]
        run = 1
    if g - f + 1 > best:
        best = g - f + 1
    g = g + 1

print(best)