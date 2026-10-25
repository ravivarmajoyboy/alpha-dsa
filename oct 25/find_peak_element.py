n = int(input("Enter size: "))
nums = []

for i in range(n):
    val = int(input("Enter number: "))
    nums.append(val)

left = 0
right = n - 1

while left < right:
    mid = left + (right - left) // 2

    if nums[mid] < nums[mid + 1]:
        left = mid + 1
    else:
        right = mid

print(left)