n = int(input("Enter size: "))
nums = []

for i in range(n):
    value = int(input("Enter number: "))
    nums.append(value)

target = int(input("Enter target: "))

left = 0
right = n - 1
result = -1

while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] == target:
        result = mid
        break

    if nums[left] <= nums[mid]:
        if nums[left] <= target and target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target and target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

print(result)