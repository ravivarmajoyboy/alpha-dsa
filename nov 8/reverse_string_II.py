text = input("Enter a string: ")
k = int(input("Enter k: "))

chars = []

for ch in text:
    chars.append(ch)

i = 0
n = len(chars)

while i < n:
    left = i
    right = i + k - 1

    if right >= n:
        right = n - 1

    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp

        left += 1
        right -= 1

    i = i + 2 * k

result = "".join(chars)

print("Result:", result)