text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

chars = []

for ch in freq:
    chars.append(ch)

for i in range(len(chars)):
    for j in range(0, len(chars) - i - 1):
        if freq[chars[j]] < freq[chars[j + 1]]:
            temp = chars[j]
            chars[j] = chars[j + 1]
            chars[j + 1] = temp

result = ""

for ch in chars:
    result = result + ch * freq[ch]

print("Output:", result)