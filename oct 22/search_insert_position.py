n = int(input("Enter size: "))
arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

target = int(input("Enter target: "))

lo = 0
hi = n - 1
position = n

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if arr[mid] >= target:
        position = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(position)