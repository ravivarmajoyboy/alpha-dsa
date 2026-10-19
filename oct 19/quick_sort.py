n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

stack = []
stack.append(0)
stack.append(n - 1)

while len(stack) > 0:
    high = stack.pop()
    low = stack.pop()

    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp

        p = i + 1

        if p - 1 > low:
            stack.append(low)
            stack.append(p - 1)

        if p + 1 < high:
            stack.append(p + 1)
            stack.append(high)

print(arr)