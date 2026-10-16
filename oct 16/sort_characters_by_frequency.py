s = input("Enter string: ")

chars = []
freq = []

for ch in s:
    found = False

    for i in range(len(chars)):
        if chars[i] == ch:
            freq[i] += 1
            found = True
            break

    if found == False:
        chars.append(ch)
        freq.append(1)

for i in range(len(freq)):
    big = i

    for j in range(i + 1, len(freq)):
        if freq[j] > freq[big]:
            big = j

    temp = freq[i]
    freq[i] = freq[big]
    freq[big] = temp

    temp = chars[i]
    chars[i] = chars[big]
    chars[big] = temp

result = ""

for i in range(len(chars)):
    for j in range(freq[i]):
        result += chars[i]

print(result)