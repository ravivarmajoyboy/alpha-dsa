s = input("Enter string: ")
p = input("Enter pattern: ")

need = {}
window = {}

for ch in p:
    need[ch] = need.get(ch, 0) + 1

left = 0
result = []

for right in range(len(s)):
    ch = s[right]
    window[ch] = window.get(ch, 0) + 1

    if right - left + 1 > len(p):
        old = s[left]
        window[old] -= 1

        if window[old] == 0:
            del window[old]

        left += 1

    if window == need:
        result.append(left)

print(result)