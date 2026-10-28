n = int(input("Enter number of piles: "))
piles = []

for i in range(n):
    a = int(input("Enter pile size: "))
    piles.append(a)

h = int(input("Enter available hours: "))

left = 1
right = max(piles)

while left < right:
    speed = (left + right) // 2
    hours = 0

    for p in piles:
        hours += p // speed

        if p % speed != 0:
            hours += 1

    if hours <= h:
        right = speed
    else:
        left = speed + 1

print("Minimum eating speed:", left)