n = int(input("Enter total versions: "))
bad = int(input("Enter first bad version: "))

lo = 1
hi = n
answer = n

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if mid >= bad:
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)