size = int(input("Enter number of elements: "))
nums = []

for i in range(size):
    val = int(input("Enter number: "))
    nums.append(val)

for i in range(1, size):
    current = nums[i]
    pos = i - 1

    while pos >= 0 and nums[pos] > current:
        nums[pos + 1] = nums[pos]
        pos -= 1

    nums[pos + 1] = current

print(nums)