total = int(input("Enter number of intervals: "))
ranges = []

for i in range(total):
    x = int(input("Enter start: "))
    y = int(input("Enter end: "))
    ranges.append([x, y])

# Insertion sort by ending value
for i in range(1, total):
    hold = ranges[i]
    j = i - 1

    while j >= 0 and ranges[j][1] > hold[1]:
        ranges[j + 1] = ranges[j]
        j -= 1

    ranges[j + 1] = hold

removed = 0
last_end = float("-inf")

for item in ranges:
    if item[0] < last_end:
        removed += 1
    else:
        last_end = item[1]

print("Intervals to remove:", removed)