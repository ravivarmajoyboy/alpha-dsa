num = int(input("Enter number: "))

lo = 0
hi = num
found = False

if num >= 0:
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if mid * mid == num:
            found = True
            break
        elif mid * mid < num:
            lo = mid + 1
        else:
            hi = mid - 1

print(found)