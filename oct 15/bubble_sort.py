n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    x = int(input("Enter number: "))
    arr.append(x)

for i in range(n):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)