def count_inversions(arr, left, right):
    total = 0

    if left < right:
        mid = (left + right) // 2

        total += count_inversions(arr, left, mid)
        total += count_inversions(arr, mid + 1, right)

        a = arr[left:mid + 1]
        b = arr[mid + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                total += len(a) - i
                j += 1

            k += 1

        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1

        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1

    return total


n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input()))

ans = count_inversions(nums, 0, n - 1)

print(ans)