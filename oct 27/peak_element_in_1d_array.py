size = int(input("Enter size: "))
values = []

for i in range(size):
    item = int(input("Enter number: "))
    values.append(item)

start = 0
end = size - 1

while start < end:
    center = start + (end - start) // 2

    if values[center] < values[center + 1]:
        start = center + 1
    else:
        end = center

print(start)