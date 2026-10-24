n = int(input("Enter size: "))
nums = []

for i in range(n):
    value = int(input("Enter number: "))
    nums.append(value)

target = int(input("Enter target: "))

lo = 0
hi = n - 1
start = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if nums[mid] >= target:
        if nums[mid] == target:
            start = mid
        hi = mid - 1
    else:
        lo = mid + 1

lo = 0
hi = n - 1
end = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if nums[mid] <= target:
        if nums[mid] == target:
            end = mid
        lo = mid + 1
    else:
        hi = mid - 1

if start == -1:
    print(0)
else:
    print(end - start + 1)