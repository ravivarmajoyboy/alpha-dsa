n = int(input("Enter number of intervals: "))
blocks = []

for i in range(n):
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    blocks.append([start, end])

new_start = int(input("Enter new interval start: "))
new_end = int(input("Enter new interval end: "))

result = []
i = 0

# Add intervals before the new interval
while i < n and blocks[i][1] < new_start:
    result.append(blocks[i])
    i += 1

# Merge overlapping intervals
while i < n and blocks[i][0] <= new_end:
    if blocks[i][0] < new_start:
        new_start = blocks[i][0]

    if blocks[i][1] > new_end:
        new_end = blocks[i][1]

    i += 1

result.append([new_start, new_end])

# Add remaining intervals
while i < n:
    result.append(blocks[i])
    i += 1

print("Final intervals:")
for item in result:
    print(item[0], item[1])