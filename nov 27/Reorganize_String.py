
word = input("Enter a string: ")

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

result = ""
previous = ""

for i in range(len(word)):

    highest = 0
    selected = ""

    for ch in freq:
        if freq[ch] > highest and ch != previous:
            highest = freq[ch]
            selected = ch

    if selected == "":
        result = ""
        break

    result = result + selected
    freq[selected] = freq[selected] - 1
    previous = selected

print("Output:", result)