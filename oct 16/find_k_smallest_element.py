size = int(input("Enter number of elements: "))
nums = []

for i in range(size):
    val = int(input("Enter number: "))
    nums.append(val)

k = int(input("Enter k: "))

for i in range(k):
    small = i

    for j in range(i + 1, size):
        if nums[j] < nums[small]:
            small = j

    temp = nums[i]
    nums[i] = nums[small]
    nums[small] = temp

print(nums[:k])