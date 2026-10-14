s = input("Enter string: ")
k = int(input("Enter k: "))

count = {}
left = 0
max_freq = 0
max_len = 0

for right in range(len(s)):
    ch = s[right]
    count[ch] = count.get(ch, 0) + 1

    if count[ch] > max_freq:
        max_freq = count[ch]

    while (right - left + 1) - max_freq > k:
        old = s[left]
        count[old] -= 1
        left += 1

    length = right - left + 1

    if length > max_len:
        max_len = length

print(max_len)