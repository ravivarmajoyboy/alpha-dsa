n = int(input("Enter size: "))
arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

target = int(input("Enter target: "))

left = 0
right = n - 1

while left < right:
    mid = left + (right - left) // 2

    if arr[mid] < arr[mid + 1]:
        left = mid + 1
    else:
        right = mid

peak = left
answer = -1

left = 0
right = peak

while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == target:
        answer = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if answer == -1:
    left = peak + 1
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            answer = mid
            break
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

print(answer)