def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

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


n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    x = int(input("Enter number: "))
    nums.append(x)

merge_sort(nums, 0, n - 1)

print(nums)