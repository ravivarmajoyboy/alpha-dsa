n = int(input("Enter n: "))
secret = int(input("Enter secret number: "))

lo = 1
hi = n
answer = -1

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if mid < secret:
        lo = mid + 1
    elif mid > secret:
        hi = mid - 1
    else:
        answer = mid
        break

print(answer)