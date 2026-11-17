word = input("Enter a string: ")

vowels = "aeiou"
prefix = [0]

for ch in word:
    count = prefix[-1]

    if ch in vowels:
        count = count + 1

    prefix.append(count)

q = int(input("Enter number of queries: "))

for i in range(q):
    left = int(input("Enter left index: "))
    right = int(input("Enter right index: "))

    ans = prefix[right + 1] - prefix[left]

    print("Vowels:", ans)