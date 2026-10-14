n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    x = int(input())
    nums.append(x)

k = int(input("Enter k: "))

left = 0
zeros = 0
max_len = 0

for right in range(n):
    if nums[right] == 0:
        zeros += 1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1
        left += 1

    length = right - left + 1

    if length > max_len:
        max_len = length

print(max_len)