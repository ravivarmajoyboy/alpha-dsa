rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid elements:")

for i in range(rows):
    line = []

    for j in range(cols):
        value = input()
        line.append(value)

    grid.append(line)

k = int(input("Enter number of shifts: "))

total = rows * cols
flat = []

for i in range(rows):
    for j in range(cols):
        flat.append(grid[i][j])

shifted = [0] * total

for i in range(total):
    new_pos = (i + k) % total
    shifted[new_pos] = flat[i]

result = []
index = 0

for i in range(rows):
    line = []

    for j in range(cols):
        line.append(shifted[index])
        index = index + 1

    result.append(line)

print("Output:")

for line in result:
    print(line)