size = int(input("Enter size: "))
mountain = []

for i in range(size):
    num = int(input("Enter number: "))
    mountain.append(num)

low = 0
high = size - 1

while low < high:
    center = low + (high - low) // 2

    if mountain[center] < mountain[center + 1]:
        low = center + 1
    else:
        high = center

print(low)