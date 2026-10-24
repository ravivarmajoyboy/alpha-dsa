n = int(input("Enter size: "))
arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

target = int(input("Enter target: "))

lo = 0
hi = n - 1
first = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] == target:
        first = mid
        hi = mid - 1
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

lo = 0
hi = n - 1
last = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] == target:
        last = mid
        lo = mid + 1
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1

print([first, last])