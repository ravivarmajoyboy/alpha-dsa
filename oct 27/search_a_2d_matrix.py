rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    line = []
    for j in range(cols):
        num = int(input("Enter number: "))
        line.append(num)
    matrix.append(line)

target = int(input("Enter target: "))

low = 0
high = rows * cols - 1
found = False

while low <= high:
    mid = low + (high - low) // 2

    r = mid // cols
    c = mid % cols

    if matrix[r][c] == target:
        found = True
        break
    elif matrix[r][c] < target:
        low = mid + 1
    else:
        high = mid - 1

print(found)