n = int(input("Enter number of packages: "))
weights = []

for i in range(n):
    x = int(input("Enter weight: "))
    weights.append(x)

days = int(input("Enter number of days: "))

low = max(weights)
high = sum(weights)

while low < high:
    mid = (low + high) // 2

    day_count = 1
    current = 0

    for w in weights:
        if current + w > mid:
            day_count += 1
            current = w
        else:
            current += w

    if day_count <= days:
        high = mid
    else:
        low = mid + 1

print("Minimum capacity:", low)