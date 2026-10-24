n = int(input("Enter size: "))
arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

target = int(input("Enter target: "))

lo = 0
hi = n - 1
floor_value = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] <= target:
        floor_value = arr[mid]
        lo = mid + 1
    else:
        hi = mid - 1

lo = 0
hi = n - 1
ceil_value = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] >= target:
        ceil_value = arr[mid]
        hi = mid - 1
    else:
        lo = mid + 1

print("Floor:", floor_value)
print("Ceiling:", ceil_value)