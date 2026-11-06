word = input("Enter string: ")

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

total = 0
odd = 0

for ch in freq:
    if freq[ch] % 2 == 0:
        total += freq[ch]
    else:
        total += freq[ch] - 1
        odd = 1

total = total + odd

print("Longest palindrome length:", total)