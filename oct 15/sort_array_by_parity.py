n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

for i in range(n):
    for j in range(n - 1 - i):
        if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)