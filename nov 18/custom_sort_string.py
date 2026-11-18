order = input("Enter order string: ")
text = input("Enter another string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

result = ""

for ch in order:
    if ch in freq:
        result = result + ch * freq[ch]
        freq[ch] = 0

for ch in text:
    if freq[ch] > 0:
        result = result + ch
        freq[ch] = freq[ch] - 1

print("Output:", result)