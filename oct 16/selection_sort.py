n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    x = int(input("Enter number: "))
    arr.append(x)

for i in range(n):
    small = i

    for j in range(i + 1, n):
        if arr[j] < arr[small]:
            small = j

    temp = arr[i]
    arr[i] = arr[small]
    arr[small] = temp

print(arr)