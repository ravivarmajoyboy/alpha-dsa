jewels = input("Enter jewels: ")
stones = input("Enter stones: ")

jewel_count = {}

for ch in jewels:
    jewel_count[ch] = 1

total = 0

for ch in stones:
    if ch in jewel_count:
        total += 1

print("Number of jewels:", total)