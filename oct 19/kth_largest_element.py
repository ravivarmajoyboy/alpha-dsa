n = int(input("Enter number of elements: "))
values = []

for i in range(n):
    values.append(int(input()))

k = int(input("Enter k: "))

target = n - k
left = 0
right = n - 1
found = False

while left <= right:
    pivot = values[right]
    i = left - 1

    for j in range(left, right):
        if values[j] <= pivot:
            i += 1
            temp = values[i]
            values[i] = values[j]
            values[j] = temp

    temp = values[i + 1]
    values[i + 1] = values[right]
    values[right] = temp

    p = i + 1

    if p == target:
        print(values[p])
        found = True
        break

    elif p < target:
        left = p + 1

    else:
        right = p - 1

if found == False:
    print("Invalid k")