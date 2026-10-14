s = input("Enter string: ")

seen = {}
left = 0
max_len = 0

for right in range(len(s)):
    ch = s[right]

    if ch in seen and seen[ch] >= left:
        left = seen[ch] + 1

    seen[ch] = right

    length = right - left + 1

    if length > max_len:
        max_len = length

print(max_len)