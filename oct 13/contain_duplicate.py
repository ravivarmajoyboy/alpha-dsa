nums = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

k = int(input("Enter k: "))
found = False

for i in range(len(nums)):
    for j in range(i + 1, min(i + k + 1, len(nums))):
        if nums[i] == nums[j]:
            found = True
            break

    if found:
        break

print(found)