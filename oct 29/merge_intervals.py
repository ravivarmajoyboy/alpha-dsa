n = int(input("Enter number of intervals: "))
arr = []

for i in range(n):
    a = int(input("Enter start: "))
    b = int(input("Enter end: "))
    arr.append([a, b])

# Insertion sort
for i in range(1, n):
    temp = arr[i]
    j = i - 1

    while j >= 0 and arr[j][0] > temp[0]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = temp

ans = []

for pair in arr:
    if len(ans) == 0:
        ans.append(pair)
    elif pair[0] <= ans[-1][1]:
        if pair[1] > ans[-1][1]:
            ans[-1][1] = pair[1]
    else:
        ans.append(pair)

print("Merged intervals:")
for pair in ans:
    print(pair[0], pair[1])