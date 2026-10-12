m = int(input("enter the total number: "))
b = []
for k in range(m):
    b.append(int(input("enter the number: ")))
p = int(input("enter the wanted sum: "))

seen = {}
seen[0] = -1
total = 0
big = 0

for x in range(m):
    total = total + b[x]
    if total - p in seen:
        if x - seen[total - p] > big:
            big = x - seen[total - p]
    if total not in seen:
        seen[total] = x

print(big)