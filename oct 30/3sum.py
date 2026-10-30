size = int(input("Enter number of elements: "))
arr = []

for i in range(size):
    num = int(input("Enter number: "))
    arr.append(num)

for i in range(1, size):
    value = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > value:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = value

found = False

for i in range(size - 2):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = size - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if total == 0:
            print(arr[i], arr[left], arr[right])
            found = True

            a = arr[left]
            b = arr[right]

            while left < right and arr[left] == a:
                left += 1

            while left < right and arr[right] == b:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

if found == False:
    print("No triplets found")