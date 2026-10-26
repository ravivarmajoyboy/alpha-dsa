size = int(input("Enter size: "))
arr = []

for i in range(size):
    num = int(input("Enter number: "))
    arr.append(num)

low = 0
high = size - 1

while low < high:
    center = low + (high - low) // 2

    if arr[center] > arr[high]:
        low = center + 1
    else:
        high = center

print(arr[low])