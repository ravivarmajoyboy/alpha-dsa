n = int(input("Enter size: "))
arr = []

for i in range(n):
    value = int(input("Enter number: "))
    arr.append(value)

freq = {}

for value in arr:
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1

for i in range(n - 1):
    for j in range(n - 1 - i):
        if freq[arr[j]] > freq[arr[j + 1]]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

        elif freq[arr[j]] == freq[arr[j + 1]]:
            if arr[j] < arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

print("Sorted by frequency:", arr)