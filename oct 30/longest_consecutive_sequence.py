n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    val = int(input("Enter number: "))
    nums.append(val)

for i in range(1, n):
    temp = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > temp:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = temp

longest = 0
count = 0
previous = None

for x in nums:
    if previous is None:
        count = 1
    elif x == previous:
        continue
    elif x == previous + 1:
        count += 1
    else:
        count = 1

    previous = x

    if count > longest:
        longest = count

print("Longest consecutive sequence:", longest)