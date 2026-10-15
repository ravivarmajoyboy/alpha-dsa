size = int(input("Enter number of elements: "))
nums = []

for i in range(size):
    val = int(input("Enter number: "))
    nums.append(val)

for i in range(size):
    swapped = False

    for j in range(size - 1 - i):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
            swapped = True

    if swapped == False:
        break

print(nums)