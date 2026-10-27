m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

grid = []

for i in range(m):
    row_data = []
    for j in range(n):
        bit = int(input("Enter 0 or 1: "))
        row_data.append(bit)
    grid.append(row_data)

best_row = -1
most_ones = 0

for i in range(m):
    left = 0
    right = n - 1
    first_one = n

    while left <= right:
        mid = left + (right - left) // 2

        if grid[i][mid] == 1:
            first_one = mid
            right = mid - 1
        else:
            left = mid + 1

    total = n - first_one

    if total > most_ones:
        most_ones = total
        best_row = i

print(best_row)