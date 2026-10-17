n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter 0, 1 or 2: "))
    arr.append(num)

for i in range(1, n):
    value = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > value:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = value

print(arr)