n = int(input("Enter size: "))
values = []

for i in range(n):
    item = int(input("Enter number: "))
    values.append(item)

start = 0
end = n - 1

while start < end:
    middle = start + (end - start) // 2

    if values[middle] > values[end]:
        start = middle + 1
    else:
        end = middle

print(start)