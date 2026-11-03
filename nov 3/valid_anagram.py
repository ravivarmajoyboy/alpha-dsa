first = input("Enter first string: ")
second = input("Enter second string: ")

freq1 = {}
freq2 = {}

for ch in first:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1

for ch in second:
    if ch in freq2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1

if freq1 == freq2:
    print("Valid Anagram")
else:
    print("Not an Anagram")