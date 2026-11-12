words = input("Enter words separated by space: ").split()

encoded = ""

for word in words:
    encoded += str(len(word)) + "#" + word

print("Encoded string:", encoded)

decoded = []
i = 0

while i < len(encoded):
    j = i

    while encoded[j] != "#":
        j += 1

    length = int(encoded[i:j])
    word = encoded[j + 1:j + 1 + length]

    decoded.append(word)
    i = j + 1 + length

print("Decoded strings:", decoded)