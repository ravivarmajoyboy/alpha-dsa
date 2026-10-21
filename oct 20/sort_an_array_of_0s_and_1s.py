n = int(input("Enter size: "))
nums = []

for i in range(n):
    x = int(input("Enter 0 or 1: "))
    nums.append(x)

zeros = 0

for x in nums:
    if x == 0:
        zeros += 1

for i in range(n):
    if i < zeros:
        nums[i] = 0
    else:
        nums[i] = 1

print("Sorted array:", nums)