n = int(input("Enter size: "))
colors = []

for i in range(n):
    value = int(input("Enter 0, 1 or 2: "))
    colors.append(value)

left = 0
mid = 0
right = n - 1

while mid <= right:
    if colors[mid] == 0:
        temp = colors[left]
        colors[left] = colors[mid]
        colors[mid] = temp
        left += 1
        mid += 1

    elif colors[mid] == 1:
        mid += 1

    else:
        temp = colors[mid]
        colors[mid] = colors[right]
        colors[right] = temp
        right -= 1

print("Sorted colors:", colors)