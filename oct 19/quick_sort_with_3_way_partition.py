size = int(input("Enter number of elements: "))
nums = []

for i in range(size):
    nums.append(int(input()))

stack = []
stack.append(0)
stack.append(size - 1)

while len(stack) > 0:
    right = stack.pop()
    left = stack.pop()

    if left < right:
        pivot = nums[right]
        low = left
        mid = left
        high = right

        while mid <= high:
            if nums[mid] < pivot:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                low += 1
                mid += 1

            elif nums[mid] > pivot:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -= 1

            else:
                mid += 1

        if left < low - 1:
            stack.append(left)
            stack.append(low - 1)

        if high + 1 < right:
            stack.append(high + 1)
            stack.append(right)

print(nums)