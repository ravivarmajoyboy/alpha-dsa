s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

need = {}
window = {}

for ch in s1:
    need[ch] = need.get(ch, 0) + 1

left = 0
found = False

for right in range(len(s2)):
    ch = s2[right]
    window[ch] = window.get(ch, 0) + 1

    if right - left + 1 > len(s1):
        old = s2[left]
        window[old] -= 1

        if window[old] == 0:
            del window[old]

        left += 1

    if window == need:
        found = True
        break

print(found)