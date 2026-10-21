n = int(input("Enter size: "))
nums = []

for i in range(n):
    value = int(input("Enter number: "))
    nums.append(value)

for i in range(n - 1):
    if i % 2 == 0:
        if nums[i] > nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
    else:
        if nums[i] < nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp

print("Wiggle array:", nums)